# Free Proxy List

Fresh verified **HTTP**, **HTTPS**, **SOCKS4** and **SOCKS5** proxies for developers.
Updated automatically, available as **JSON**, **TXT** and **CSV**, and usable without signup.

[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/xyzs996/free-proxy-health-list?style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/commits/main)
[![License](https://img.shields.io/github/license/xyzs996/free-proxy-health-list?style=for-the-badge)](./LICENSE)
[![Proxy API](https://img.shields.io/badge/Proxy_API-early_access-0ea5e9?style=for-the-badge)](#need-higher-reliability)

> Latest snapshot: see [`stats/latest.json`](./stats/latest.json).
> The public list is free forever. Stars are optional support and never required.

[English](./README.md) | [中文](./README_CN.md)

## Download

Use jsDelivr after publishing the repository:

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt -o proxies.txt
```

| Type | TXT | JSON | CSV |
| --- | --- | --- | --- |
| All proxies | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.csv) |
| HTTP | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.csv) |
| HTTPS | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.csv) |
| SOCKS4 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.csv) |
| SOCKS5 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.csv) |
| Fast proxies | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.csv) |
| Top 1000 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.csv) |

## Why This Project

Most free proxy lists only answer one question: "is this proxy alive right now?"
ProxyHealthList is designed to answer the questions developers actually care about:

- How fresh is the proxy list?
- Which protocol does each proxy support?
- How fast was the last check?
- Was it verified through HTTP or only a TCP reachability check?
- Can I consume the data from GitHub, CDN, scripts or an API?

The first public version focuses on safe, developer-friendly metadata: protocol,
latency, check type, quality score and update time. More quality signals can be
added without changing the simple TXT format.

## Data Shape

`data.txt` contains one `host:port` per line. `data.json` contains richer records:

```json
{
  "proxy": "1.2.3.4:8080",
  "host": "1.2.3.4",
  "port": 8080,
  "protocol": "https",
  "latencyMs": 842,
  "qualityScore": 91,
  "checkType": "http",
  "supportsHttps": true,
  "country": "ZZ",
  "anonymity": "unknown",
  "lastChecked": "2026-07-08T10:15:00Z",
  "source": "public"
}
```

## Published Files

This public repository is the distribution layer. It contains generated proxy
snapshots, stats, examples and user-facing documentation.

The maintenance pipeline is not part of this public repository. This keeps
source management, update logic and operational notes separate from the public
data surface.

## Examples

- [curl](./examples/curl/examples.sh)
- [Python requests](./examples/python/requests_example.py)
- [Node.js fetch](./examples/nodejs/fetch-example.mjs)
- [Playwright](./examples/playwright/playwright-example.py)
- [Scrapy](./examples/scrapy/settings.py)

## Need Higher Reliability?

The GitHub list is a free public snapshot with no SLA. For production use, the
Pro API should provide fresher checks, filtering, rotation endpoints, higher
limits and usage monitoring.

Planned API shape:

```shell
curl "https://api.freeproxy.ai/v1/proxy?protocol=socks5&max_latency=1000&limit=10" \
  -H "Authorization: Bearer $FREEPROXYAI_API_KEY"
```

The free repository stays useful on its own. The paid layer is for real-time
quality, filtering, reliability and support.

## Responsible Use

Please follow the [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies).
Do not use this project to spam, attack services, bypass access controls, mass
register accounts, scrape against website policies, or perform illegal activity.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=xyzs996/free-proxy-health-list&type=Date)](https://www.star-history.com/#xyzs996/free-proxy-health-list&Date)

## Contributing

Contributions are welcome for docs, examples and public data usability. See
[CONTRIBUTING.md](./CONTRIBUTING.md).
