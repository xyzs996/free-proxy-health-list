from __future__ import annotations

import argparse
from pathlib import Path

from .checker import check_candidates
from .publisher import publish
from .sources import collect_candidates, load_sources


def update(args: argparse.Namespace) -> int:
    source_urls = load_sources(Path(args.sources))
    candidates = collect_candidates(source_urls, limit=args.limit)
    records = check_candidates(
        candidates,
        workers=args.workers,
        timeout=args.timeout,
        test_url=args.test_url,
    )
    publish(records, root=Path(args.output), top_limit=args.top_limit)
    print(f"Collected {len(candidates)} candidates; published {len(records)} working proxies.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ProxyHealthList proxy list publisher")
    subparsers = parser.add_subparsers(dest="command", required=True)

    update_parser = subparsers.add_parser("update", help="collect, check and publish proxy files")
    update_parser.add_argument("--sources", default="sources/default_sources.txt")
    update_parser.add_argument("--output", default=".")
    update_parser.add_argument("--limit", type=int, default=2000)
    update_parser.add_argument("--workers", type=int, default=100)
    update_parser.add_argument("--timeout", type=float, default=5.0)
    update_parser.add_argument("--top-limit", type=int, default=1000)
    update_parser.add_argument("--test-url", default="http://example.com/")
    update_parser.set_defaults(func=update)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
