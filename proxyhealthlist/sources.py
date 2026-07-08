from __future__ import annotations

import re
import urllib.error
import urllib.request
from math import ceil
from pathlib import Path

from .models import ProxyCandidate

PROXY_RE = re.compile(
    r"(?:(?P<protocol>https?|socks4|socks5)://)?"
    r"(?P<host>(?:\d{1,3}\.){3}\d{1,3}|[a-zA-Z0-9.-]+)"
    r":(?P<port>\d{2,5})"
)


def load_sources(path: Path) -> list[str]:
    urls: list[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        urls.append(line)
    return urls


def fetch_text(url: str, timeout: float = 12.0) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "proxyhealthlist/0.1 (+https://github.com/xyzs996/free-proxy-health-list)"
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError):
        return ""


def parse_candidates(text: str, source: str, default_protocol: str = "http") -> list[ProxyCandidate]:
    candidates: list[ProxyCandidate] = []
    for match in PROXY_RE.finditer(text):
        protocol = (match.group("protocol") or default_protocol).lower()
        host = match.group("host")
        port = int(match.group("port"))
        if port < 1 or port > 65535:
            continue
        candidates.append(
            ProxyCandidate(host=host, port=port, protocol=protocol, source=source)
        )
    return candidates


def infer_protocol_from_source(url: str) -> str:
    lowered = url.lower()
    tail = lowered.rsplit("/", maxsplit=1)[-1]
    if "socks5" in tail:
        return "socks5"
    if "socks4" in tail:
        return "socks4"
    if "https" in tail:
        return "https"
    if "http" in tail:
        return "http"
    return "http"


def collect_candidates(source_urls: list[str], limit: int | None = None) -> list[ProxyCandidate]:
    seen: set[tuple[str, int, str]] = set()
    collected: list[ProxyCandidate] = []
    per_source_limit = ceil(limit / len(source_urls)) if limit and source_urls else None

    for url in source_urls:
        text = fetch_text(url)
        if not text:
            continue
        default_protocol = infer_protocol_from_source(url)
        source_count = 0
        for candidate in parse_candidates(text, source=url, default_protocol=default_protocol):
            key = (candidate.host, candidate.port, candidate.protocol)
            if key in seen:
                continue
            seen.add(key)
            collected.append(candidate)
            source_count += 1
            if per_source_limit and source_count >= per_source_limit:
                break

    return collected[:limit] if limit else collected
