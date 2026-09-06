<!-- proxyhealthlist:generated — rebuilt by `proxyhealthlist build-site` from the published
     snapshot. Hand edits are overwritten on the next run; change the
     generator (proxyhealthlist/site/) or open an issue instead. -->
<div align="center">

<a href="https://xyzs996.github.io/free-proxy-health-list/"><img src="./assets/og-image.png" alt="Free Proxy List — Verified HTTP, HTTPS, SOCKS4 and SOCKS5 Proxies" width="100%"></a>

# Free Proxy Health List

**The free proxy list that is actually verified.**

[![total](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/total.json) [![http](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/http.json) [![socks5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/socks5.json) [![updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/updated.json) [![reliability](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Freliability.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/reliability.json)
[![Validate snapshot](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml/badge.svg)](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

[🌐 Download](https://xyzs996.github.io/free-proxy-health-list/) · [⚡ Pro API](https://xyzs996.github.io/free-proxy-health-list/api.html) · [📊 What does an AI agent cost to run?](https://github.com/xyzs996/llm-api-pricing) · [💬 Which country do you need?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README.md) · [🐞 Issues](https://github.com/xyzs996/free-proxy-health-list/issues)

**English** · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md) · [Русский](./README_RU.md) · [Türkçe](./README_TR.md) · [Bahasa Indonesia](./README_ID.md) · [Tiếng Việt](./README_VI.md)

</div>

> Public snapshot · updated every 30 minutes · no signup

## 💡 Why this project?

A while back I was building a small price-tracking scraper. Every run kept getting rate-limited from my single IP, so I went looking for free proxies. Every list told the same story: half the entries were dead, the "updated daily" ones had not moved in months, and the sites with working proxies wanted a credit card before I could even test one.

I already ran automated health checks for my own scraping, so I started publishing the results — a free proxy list that is **actually verified**, re-checked every 30 minutes, and pullable from a stable CDN link. No signup, no credit card, no dashboard. That is all this is. If it saves you the afternoon I lost, a star helps the next developer find it. The data is free either way.

## 🚀 Copy and use

One command per format. Stable paths that never move.

```shell
# All proxies
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt -o proxies.txt

# SOCKS5
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt -o socks5.txt
```

## 📦 Download files

| List | Proxies | TXT | JSON | CSV | CDN |
| --- | --- | --- | --- | --- | --- |
| **All proxies** | `4,196` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) |
| HTTP | `1,090` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/http.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) |
| HTTPS | `1,587` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/https.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) |
| SOCKS4 | `930` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks4.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) |
| SOCKS5 | `589` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) |
| Fast proxies | `790` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) |
| Stable proxies | `1,550` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/stability/stable/data.txt) |
| Elite proxies | `2,998` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/anonymity/elite/data.txt) |

**Browse by country:** [Indonesia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/id/data.txt), [United States](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/us/data.txt), [China](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/cn/data.txt), [India](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/in/data.txt), [Bangladesh](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/bd/data.txt), [Philippines](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ph/data.txt), [Mexico](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/mx/data.txt), [Brazil](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/br/data.txt), [Colombia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/co/data.txt), [Vietnam](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/vn/data.txt), [Germany](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/de/data.txt), [Russia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ru/data.txt), [Thailand](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/th/data.txt), [Canada](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ca/data.txt), [Hong Kong](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/hk/data.txt), [Venezuela](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ve/data.txt), [France](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/fr/data.txt), [Japan](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/jp/data.txt), [Singapore](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/sg/data.txt), [Netherlands](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/nl/data.txt), [Ecuador](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ec/data.txt), [Italy](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/it/data.txt), [Cambodia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/kh/data.txt), [Spain](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/es/data.txt) — [View all](https://github.com/xyzs996/free-proxy-health-list/tree/main/proxies/countries)

## 📊 Measured working rate

Most proxy lists claim to be verified and none publish a number. This one does: a random sample of the published list is fetched end to end through each proxy against a third-party URL, and the result ships with the data.

<img src="./assets/reliability-chart.png" width="640" alt="Measured working rate">

| List | Working in sample |
| --- | --- |
| **Latest sample** | **40%** (sampled 400) |

<sub>Method: random sample, end-to-end fetch through the proxy, 8s timeout — `http://api.ipify.org/, http://icanhazip.com/, https://api.ipify.org/, https://icanhazip.com/`</sub>

## 🧭 Guides by use case

- **[Proxies for web scraping](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-web-scraping.html)** — Rotate IPs to avoid rate limits and IP bans.
- **[Python requests proxy](https://xyzs996.github.io/free-proxy-health-list/use-cases/python-requests-proxy.html)** — HTTP and SOCKS5 examples with retry handling.
- **[Build a rotating proxy pool](https://xyzs996.github.io/free-proxy-health-list/use-cases/rotating-proxy.html)** — A working rotation loop in about 20 lines.
- **[Scrapy proxy middleware](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-scrapy.html)** — Drop-in middleware that rotates on failure.
- **[curl proxy flags](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-curl.html)** — HTTP, HTTPS and SOCKS flags with real commands.

## 🌐 Browse by protocol

- [HTTP](https://xyzs996.github.io/free-proxy-health-list/protocols/http.html) — Simplest for web requests. Works with every HTTP client.
- [HTTPS](https://xyzs996.github.io/free-proxy-health-list/protocols/https.html) — HTTP proxies verified to tunnel TLS via CONNECT.
- [SOCKS4](https://xyzs996.github.io/free-proxy-health-list/protocols/socks4.html) — Lightweight legacy tunnel for raw TCP.
- [SOCKS5](https://xyzs996.github.io/free-proxy-health-list/protocols/socks5.html) — Any TCP traffic, plus UDP and remote DNS.

## 🧱 Data shape

`data.txt` holds one `host:port` per line. `data.json` carries the health metadata behind every entry:

```json
{
  "proxy": "203.0.113.10:8080",
  "host": "203.0.113.10",
  "port": 8080,
  "protocol": "http",
  "latencyMs": 842,
  "qualityScore": 91,
  "checkType": "http_probe",
  "supportsHttps": true,
  "country": "US",
  "anonymity": "elite",
  "consecutiveSuccesses": 4,
  "reliabilityScore": 96.75,
  "reliabilitySamples": 41,
  "lastChecked": "2026-07-25T11:09:35Z"
}
```

Reading this with a program? [`llms.txt`](https://xyzs996.github.io/free-proxy-health-list/llms.txt) is the whole snapshot in one request — every list with its count, its download URLs and the date it was checked.

## 🔗 Related projects

Same maintainer, same idea — public data you can read without an account:

- **[Free LLM API list](https://github.com/xyzs996/free-llm-api)** — permanent free tiers, every published limit linked to its official source.
- **[LLM API pricing list](https://github.com/xyzs996/llm-api-pricing)** — what AI coding agents actually cost. Every figure from the write-ups in [one table](https://xyzs996.github.io/llm-api-pricing/figures.html), each row carrying the sentence it came from ([JSON](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.json) / [CSV](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.csv)). Start with [where the token bill actually goes](https://xyzs996.github.io/llm-api-pricing/topics/token-optimization.html).

## ❓ Frequently asked questions

<details>
<summary><strong>Are these free proxies safe to use?</strong></summary>

Free public proxies are shared and run by unknown operators, so never send passwords, tokens or personal data through them. Use them for testing, scraping public pages and automation — not sensitive traffic.
</details>

<details>
<summary><strong>How often is the proxy list updated?</strong></summary>

Every proxy is re-checked and the list republished every 30 minutes. Each JSON record carries a lastChecked timestamp and a latency value so you can drop stale or slow entries yourself.
</details>

<details>
<summary><strong>What does 'verified' actually mean here?</strong></summary>

Each entry completed a protocol-correct handshake and relayed a real request end to end before publication. Entries that only answered a TCP connect are not published.
</details>

<details>
<summary><strong>Why do some proxies stop working within minutes?</strong></summary>

Free proxies are volatile by nature — they appear and disappear constantly. That is exactly why the list is re-checked every 30 minutes and sorted fastest-first. Always loop to the next entry on failure.
</details>

<details>
<summary><strong>Which proxy type should I use?</strong></summary>

HTTP is simplest for web requests. SOCKS5 handles any TCP traffic plus UDP and remote DNS. SOCKS4 is a lighter legacy fallback. HTTPS entries are HTTP proxies verified to tunnel TLS.
</details>

<details>
<summary><strong>Do I need to sign up or star the repository?</strong></summary>

No. The list is a fully public snapshot on stable URLs, with no account and no credit card. A star just helps other developers find it.
</details>

## 🧾 Answered at length, with the numbers

The answers above are short on purpose. These are not — each one opens with a direct answer and then shows every measured figure behind it, with the sample size and the timestamp it came from:

- [How many free proxies actually work? Here is the measured rate, by protocol.](https://github.com/xyzs996/free-proxy-health-list/discussions/2) — the measured end-to-end success rate of a random sample, broken out by protocol, with the method and the timeout it was measured under.
- [Where do I get a free proxy list by country, and how many are in each?](https://github.com/xyzs996/free-proxy-health-list/discussions/3) — the per-country file path, how many entries each country has in the current snapshot, and how thin the tail gets.
- [How do I check whether a free proxy actually works?](https://github.com/xyzs996/free-proxy-health-list/discussions/4) — a working checker in ten lines, plus the four ways a naive check calls a dead proxy alive.

## ⚡ Need production reliability?

The GitHub list is a free public snapshot with no SLA. The Pro API adds fresher checks, filtering by protocol, country and latency, a rotating endpoint and usage monitoring.

[Join early access](https://xyzs996.github.io/free-proxy-health-list/api.html)

## ⚖️ Public snapshot boundary

Free public proxies are shared and operated by unknown parties. Never send passwords, tokens or personal data through them. Follow the GitHub Acceptable Use Policies: no spam, no attacks, no bypassing access controls, no scraping against site policies.

## 🤝 Contributing

Contributions are welcome for docs, examples and data usability. See [CONTRIBUTING.md](./CONTRIBUTING.md)

No source, no screenshot and no pull request needed — [which country did you need, and did this list have it?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README.md)

## 📄 License

[MIT](./LICENSE)
