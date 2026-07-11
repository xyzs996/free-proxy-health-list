# Free Proxy Health List

Verified free proxy snapshots for developers. Download **HTTP**, **SOCKS4** and
**SOCKS5** proxies as **TXT**, **JSON** or **CSV** with no signup.

[![Proxies](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](./stats/latest.json)
[![HTTP](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](./proxies/protocols/http/data.txt)
[![SOCKS4](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fsocks4.json&style=for-the-badge)](./proxies/protocols/socks4/data.txt)
[![SOCKS5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](./proxies/protocols/socks5/data.txt)
[![Updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](./stats/latest.json)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

> Public snapshot, no signup, no credit card. Stars are optional and never required.

[Open Website](https://xyzs996.github.io/free-proxy-health-list/) |
[Pro API Early Access](https://xyzs996.github.io/free-proxy-health-list/api.html)

**Languages:** English · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md)

## Why This Project?

A while back I was building a small price-tracking scraper on the side. Every run
kept getting rate-limited from my single IP, so I went looking for free proxies.
Every list was the same story: half the entries were dead, the "updated daily"
ones hadn't moved in months, and the sites with working proxies wanted a credit
card before I could even test one.

I already ran automated health checks for my own scraping, so I started publishing
the results — a **free proxy list that is actually verified**, re-checked hourly,
and pullable from a stable CDN link. No signup, no credit card, no dashboard.

That's all this is. If it saves you the afternoon I lost, a star helps the next
developer find it. The data is free either way.

## Quick Start

Download all proxies:

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt -o proxies.txt
```

Download SOCKS5 only:

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt -o socks5.txt
```

Use the first HTTP proxy with curl:

```shell
proxy="$(curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt | head -n 1)"
curl -x "http://$proxy" -I "http://example.com/" --max-time 10
```

## Download Files

| Type | TXT | JSON | CSV |
| --- | --- | --- | --- |
| All proxies | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.csv) |
| HTTP | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.csv) |
| HTTPS | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.csv) |
| SOCKS4 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.csv) |
| SOCKS5 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.csv) |
| Fast proxies | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.csv) |
| Top 1000 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.csv) |

## Why Developers Use It

- Direct CDN links for scripts, crawlers and automation tools.
- Stable TXT, JSON and CSV paths.
- Public health metadata: protocol, latency, quality score, check type and update time.
- No account requirement for the public snapshot.
- Separate production path for users who need fresher checks, filtering and rotation.

If this saves you time, a star helps other developers find the list. The data is
free and does not require starring.

## Use It For

Common ways developers use this free proxy list — each guide has copy-paste code:

- **[Web scraping](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-web-scraping.html)** — rotate IPs to avoid rate limits and IP bans.
- **[Python `requests`](https://xyzs996.github.io/free-proxy-health-list/use-cases/python-requests-proxy.html)** — HTTP and SOCKS5 proxy examples.
- **[Rotating proxy pool](https://xyzs996.github.io/free-proxy-health-list/use-cases/rotating-proxy.html)** — build your own rotating proxy for free.
- **[Scrapy](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-scrapy.html)** — a rotating proxy middleware.
- **[curl](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-curl.html)** — HTTP, HTTPS and SOCKS proxy flags.

## Browse By Protocol

Dedicated pages with download links, code and a live count:

- [Free HTTP proxy list](https://xyzs996.github.io/free-proxy-health-list/protocols/http.html)
- [Free HTTPS proxy list](https://xyzs996.github.io/free-proxy-health-list/protocols/https.html)
- [Free SOCKS4 proxy list](https://xyzs996.github.io/free-proxy-health-list/protocols/socks4.html)
- [Free SOCKS5 proxy list](https://xyzs996.github.io/free-proxy-health-list/protocols/socks5.html)

## Data Shape

`data.txt` contains one `host:port` per line. `data.json` contains richer records:

```json
{
  "proxy": "1.2.3.4:8080",
  "host": "1.2.3.4",
  "port": 8080,
  "protocol": "http",
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

## Examples

- [curl](./examples/curl/examples.sh)
- [Python requests](./examples/python/requests_example.py)
- [Node.js fetch](./examples/nodejs/fetch-example.mjs)
- [Playwright](./examples/playwright/playwright-example.py)
- [Scrapy](./examples/scrapy/settings.py)

## Pro API Early Access

The GitHub list is a free public snapshot with no SLA. For production use, the
planned Pro API focuses on fresh checks, filtering, rotation endpoints, higher
limits and usage monitoring.

[Join Pro API early access](https://xyzs996.github.io/free-proxy-health-list/api.html)

## FAQ

**Are these free proxies safe to use?**
Free public proxies are shared and run by unknown operators, so never send
passwords, tokens or personal data through them. Use them for testing, scraping
public pages and automation — not sensitive traffic.

**How often is the list updated?**
Every proxy is re-checked and the list republished on an hourly cadence. Each
JSON record carries a `lastChecked` timestamp and a `latencyMs` value so you can
drop stale or slow entries.

**Why do some proxies stop working within minutes?**
Free proxies are volatile by nature — they appear and disappear constantly. That
is exactly why the list is health-checked hourly and sorted fastest-first. Always
loop to the next entry on failure.

**Which proxy type should I use?**
HTTP is simplest for web requests. [SOCKS5](https://xyzs996.github.io/free-proxy-health-list/protocols/socks5.html)
handles any TCP traffic plus UDP and remote DNS. SOCKS4 is a lighter legacy
fallback. HTTPS entries are HTTP proxies verified to tunnel TLS.

**Do I need to sign up or star the repo?**
No. The list is a fully public snapshot on stable CDN links, no account and no
credit card. A star just helps other developers find it.

## Responsible Use

Please follow the [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies).
Do not use this project to spam, attack services, bypass access controls, mass
register accounts, scrape against website policies, or perform illegal activity.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=xyzs996/free-proxy-health-list&type=Date)](https://www.star-history.com/#xyzs996/free-proxy-health-list&Date)

## Contributing

Contributions are welcome for docs, examples and public data usability. See
[CONTRIBUTING.md](./CONTRIBUTING.md).
