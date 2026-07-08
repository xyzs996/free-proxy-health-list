from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

from .models import ProxyRecord


def _write_txt(path: Path, records: list[ProxyRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(record.proxy for record in records) + "\n", encoding="utf-8")


def _write_json(path: Path, records: list[ProxyRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [record.to_dict() for record in records]
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_csv(path: Path, records: list[ProxyRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "proxy",
        "host",
        "port",
        "protocol",
        "latencyMs",
        "qualityScore",
        "checkType",
        "lastChecked",
        "country",
        "anonymity",
        "supportsHttps",
        "source",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(record.to_dict() for record in records)


def _write_dataset(root: Path, records: list[ProxyRecord]) -> None:
    _write_txt(root / "data.txt", records)
    _write_json(root / "data.json", records)
    _write_csv(root / "data.csv", records)


def publish(records: list[ProxyRecord], root: Path = Path("."), top_limit: int = 1000) -> None:
    now = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    proxies_root = root / "proxies"

    _write_dataset(proxies_root / "all", records)

    for protocol in ["http", "https", "socks4", "socks5"]:
        subset = [record for record in records if record.protocol == protocol]
        _write_dataset(proxies_root / "protocols" / protocol, subset)

    fast = [record for record in records if record.latencyMs <= 1000]
    elite = [record for record in records if record.anonymity == "elite"]
    top = records[:top_limit]
    _write_dataset(proxies_root / "latency" / "fast", fast)
    _write_dataset(proxies_root / "anonymity" / "elite", elite)
    _write_dataset(proxies_root / "quality" / "top-1000", top)

    protocol_counts = Counter(record.protocol for record in records)
    country_counts = Counter(record.country for record in records)
    stats_root = root / "stats"
    stats_root.mkdir(parents=True, exist_ok=True)
    latest = {
        "updatedAt": now,
        "total": len(records),
        "protocols": dict(sorted(protocol_counts.items())),
        "countries": dict(sorted(country_counts.items())),
        "fast": len(fast),
        "elite": len(elite),
        "topLimit": top_limit,
    }
    (stats_root / "latest.json").write_text(
        json.dumps(latest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (stats_root / "protocols.json").write_text(
        json.dumps(dict(sorted(protocol_counts.items())), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (stats_root / "countries.json").write_text(
        json.dumps(dict(sorted(country_counts.items())), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
