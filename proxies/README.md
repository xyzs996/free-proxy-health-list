<!-- proxyhealthlist:generated — rebuilt by `proxyhealthlist build-site`. -->
# The proxy files

Every file here is rebuilt from scratch each run — nothing is appended, so a proxy that stops passing disappears rather than lingering with an old timestamp. Each folder holds the same three shapes: `data.txt` (`ip:port`, one per line), `data.json` (the same set with latency, country, anonymity and protocol on every entry) and `data.csv`.

| Folder | What is in it |
|---|---|
| [`all/`](./all/) | everything that passed the most recent check, with no filter on top |
| [`fresh/`](./fresh/) | byte-for-byte the same set as `all` — the name the older download links use |
| [`recent/`](./recent/) | a wider window than the last check alone, published by a separate step |
| [`protocols/`](./protocols/) | the same set split into `http/`, `https/`, `socks4/`, `socks5/` |
| [`countries/`](./countries/) | one folder per ISO country code, for proxies that geolocate there |
| [`quality/`](./quality/) | `top-1000/` — the head of this snapshot, ordered by measured reliability |
| [`latency/`](./latency/) | `fast/` — round-trip at or under one second |
| [`stability/`](./stability/) | `stable/` — passed on at least two checks in a row, not once |
| [`anonymity/`](./anonymity/) | `elite/` — the ones the checker classified as elite |
| [`network/`](./network/) | `residential/` and `likely-residential/`, by network ownership — `stats/residential.json` says whether the classifier behind them ran, so an empty folder can be told from an unmeasured one |
| [`badges/`](./badges/) | small JSON files the counters in the README read |

Pull them straight from the CDN rather than cloning — the addresses are in the [README](https://github.com/xyzs996/free-proxy-health-list/blob/main/README.md), and the same data is browsable, country by country, [on the site](https://xyzs996.github.io/free-proxy-health-list/).

**Not here?** If the country you needed is missing from `countries/`, [say which one](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=proxies%2FREADME.md) — one word is a complete answer, the page you came from is already filled in, and which sources get checked next follows the answers.
