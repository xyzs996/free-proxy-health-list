from __future__ import annotations

import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from urllib.parse import urlparse

from .models import ProxyCandidate, ProxyRecord


def _now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _tcp_probe(candidate: ProxyCandidate, timeout: float) -> tuple[bool, int]:
    start = time.perf_counter()
    try:
        with socket.create_connection((candidate.host, candidate.port), timeout=timeout):
            latency_ms = int((time.perf_counter() - start) * 1000)
            return True, latency_ms
    except OSError:
        return False, int((time.perf_counter() - start) * 1000)


def _http_proxy_probe(
    candidate: ProxyCandidate,
    timeout: float,
    test_url: str,
) -> tuple[bool, int, bool]:
    parsed = urlparse(test_url)
    host = parsed.hostname or "example.com"
    path = parsed.path or "/"
    if parsed.query:
        path += f"?{parsed.query}"

    start = time.perf_counter()
    try:
        with socket.create_connection((candidate.host, candidate.port), timeout=timeout) as sock:
            sock.settimeout(timeout)
            request = (
                f"GET {test_url} HTTP/1.1\r\n"
                f"Host: {host}\r\n"
                "User-Agent: proxyhealthlist/0.1\r\n"
                "Connection: close\r\n\r\n"
            )
            sock.sendall(request.encode("ascii"))
            response = sock.recv(256)
            latency_ms = int((time.perf_counter() - start) * 1000)
            ok = response.startswith(b"HTTP/") and b" 200 " in response[:32]
            return ok, latency_ms, False
    except OSError:
        return False, int((time.perf_counter() - start) * 1000), False


def _https_connect_probe(candidate: ProxyCandidate, timeout: float) -> bool:
    try:
        with socket.create_connection((candidate.host, candidate.port), timeout=timeout) as sock:
            sock.settimeout(timeout)
            request = (
                "CONNECT example.com:443 HTTP/1.1\r\n"
                "Host: example.com:443\r\n"
                "User-Agent: proxyhealthlist/0.1\r\n\r\n"
            )
            sock.sendall(request.encode("ascii"))
            response = sock.recv(128)
            return response.startswith(b"HTTP/") and b" 200 " in response[:32]
    except OSError:
        return False


def _score(latency_ms: int, check_type: str, supports_https: bool) -> int:
    score = 100
    if latency_ms > 500:
        score -= min(50, (latency_ms - 500) // 100)
    if check_type == "tcp":
        score -= 25
    if supports_https:
        score += 5
    return max(1, min(100, score))


def check_candidate(
    candidate: ProxyCandidate,
    timeout: float = 5.0,
    test_url: str = "http://example.com/",
) -> ProxyRecord | None:
    if candidate.protocol in {"http", "https"}:
        ok, latency_ms, _ = _http_proxy_probe(candidate, timeout=timeout, test_url=test_url)
        supports_https = _https_connect_probe(candidate, timeout=timeout)
        if ok:
            check_type = "http"
        else:
            tcp_ok, latency_ms = _tcp_probe(candidate, timeout=timeout)
            if not tcp_ok:
                return None
            check_type = "tcp"
    else:
        tcp_ok, latency_ms = _tcp_probe(candidate, timeout=timeout)
        if not tcp_ok:
            return None
        supports_https = False
        check_type = "tcp"

    quality = _score(latency_ms=latency_ms, check_type=check_type, supports_https=supports_https)
    return ProxyRecord(
        proxy=candidate.endpoint,
        host=candidate.host,
        port=candidate.port,
        protocol=candidate.protocol,
        latencyMs=latency_ms,
        qualityScore=quality,
        checkType=check_type,
        supportsHttps=supports_https,
        lastChecked=_now_iso(),
        source=candidate.source,
    )


def check_candidates(
    candidates: list[ProxyCandidate],
    workers: int = 100,
    timeout: float = 5.0,
    test_url: str = "http://example.com/",
) -> list[ProxyRecord]:
    records: list[ProxyRecord] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [
            pool.submit(check_candidate, candidate, timeout, test_url)
            for candidate in candidates
        ]
        for future in as_completed(futures):
            record = future.result()
            if record:
                records.append(record)

    records.sort(key=lambda item: (-item.qualityScore, item.latencyMs, item.proxy))
    return records
