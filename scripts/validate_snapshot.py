# proxyhealthlist:generated — rebuilt by `proxyhealthlist build-site`. Do not edit by hand.
"""Validates the published snapshot against its public contract.

Run by CI on every publish. Failures mean the data is malformed, stale, or
leaking a field that is supposed to stay private — all of which matter more
than any of them being rare.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENDPOINT = re.compile(r"^(?:\d{1,3}(?:\.\d{1,3}){3}|\[[0-9a-fA-F:]+\]):\d{1,5}$")

#: Fields that exist internally and must never reach a public file.
PRIVATE_FIELDS = ("source", "classifiedIp", "classified_ip", "exitIp", "exit_ip")

#: The publisher runs every 30 minutes; a day of slack keeps a transient
#: outage from turning the badge red while still catching a real stall.
MAX_AGE_HOURS = 24

failures: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


def load_json(relative: str):
    path = ROOT / relative
    if not path.exists():
        fail(f"missing {relative}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{relative} is not valid JSON: {exc}")
        return None


def check_freshness(latest: dict) -> None:
    stamp = str(latest.get("updatedAt") or "")
    try:
        moment = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    except ValueError:
        fail(f"stats/latest.json has an unparseable updatedAt: {stamp!r}")
        return
    age = (datetime.now(timezone.utc) - moment).total_seconds() / 3600
    if age > MAX_AGE_HOURS:
        fail(f"snapshot is {age:.1f}h old (limit {MAX_AGE_HOURS}h)")


def check_dataset(relative: str) -> None:
    base = ROOT / relative
    txt, js, csv_path = base / "data.txt", base / "data.json", base / "data.csv"
    if not txt.exists():
        fail(f"missing {relative}/data.txt")
        return
    lines = [line for line in txt.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        fail(f"{relative}/data.txt is empty")
        return
    bad = [line for line in lines[:5000] if not ENDPOINT.match(line.strip())]
    if bad:
        fail(f"{relative}/data.txt has malformed endpoints, e.g. {bad[0]!r}")
    records = load_json(f"{relative}/data.json")
    if records is None:
        return
    if not isinstance(records, list) or not records:
        fail(f"{relative}/data.json must be a non-empty list")
        return
    if len(records) != len(lines):
        fail(f"{relative}: data.json has {len(records)} rows, data.txt has {len(lines)}")
    leaked = sorted({field for row in records for field in PRIVATE_FIELDS if field in row})
    if leaked:
        fail(f"{relative}/data.json leaks private fields: {leaked}")
    if csv_path.exists():
        with csv_path.open(encoding="utf-8", newline="") as handle:
            fields = csv.DictReader(handle).fieldnames or []
        leaked_csv = [field for field in PRIVATE_FIELDS if field in fields]
        if leaked_csv:
            fail(f"{relative}/data.csv leaks private fields: {leaked_csv}")


def main() -> int:
    latest = load_json("stats/latest.json")
    if isinstance(latest, dict):
        if int(latest.get("total") or 0) <= 0:
            fail("stats/latest.json reports a total of zero")
        check_freshness(latest)
    for name in ("protocols", "countries", "history"):
        load_json(f"stats/{name}.json")

    check_dataset("proxies/all")
    for protocol in ("http", "https", "socks4", "socks5"):
        if (ROOT / "proxies/protocols" / protocol / "data.txt").exists():
            check_dataset(f"proxies/protocols/{protocol}")

    if failures:
        print("Snapshot validation failed:")
        for item in failures:
            print(f"  - {item}")
        return 1
    total = latest.get("total") if isinstance(latest, dict) else "?"
    print(f"Snapshot OK: {total} proxies, contract and privacy checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
