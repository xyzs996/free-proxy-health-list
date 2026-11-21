<!-- proxyhealthlist:generated — rebuilt by `proxyhealthlist build-site`. -->
# `all/` — everything that passed the last check

The widest of the sets: every proxy that passed the most recent run, with no filter on speed, stability, anonymity or country. [`../fresh/`](../fresh/) holds the identical set under an older name. Start here if you are going to test candidates yourself, and use [`../quality/top-1000/`](../quality/top-1000/) if you would rather the cut were made for you, or [`../latency/fast/`](../latency/fast/) and [`../stability/stable/`](../stability/stable/) if you already know which of the two you care about.

- `data.txt` — `ip:port`, one per line, nothing else.
- `data.json` — the same set, each entry carrying latency, country, anonymity level and protocol.
- `data.csv` — the same fields as `data.json`, flat.

Rebuilt from scratch every run, so an entry that vanishes has stopped passing rather than been forgotten.

**Not here?** If the country you needed is missing from `countries/`, [say which one](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=proxies%2Fall%2FREADME.md) — one word is a complete answer, the page you came from is already filled in, and which sources get checked next follows the answers.
