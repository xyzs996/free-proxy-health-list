<!-- proxyhealthlist:generated — rebuilt by `proxyhealthlist build-site` from the published
     snapshot. Hand edits are overwritten on the next run; change the
     generator (proxyhealthlist/site/) or open an issue instead. -->
<div align="center">

<a href="https://xyzs996.github.io/free-proxy-health-list/zh/"><img src="./assets/og-image.png" alt="免费代理IP列表 — 已验证的 HTTP、HTTPS、SOCKS4 和 SOCKS5 代理" width="100%"></a>

# Free Proxy Health List

**真正验证过的免费代理列表。**

[![total](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/total.json) [![http](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/http.json) [![socks5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/socks5.json) [![updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/updated.json) [![reliability](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Freliability.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/reliability.json)
[![Validate snapshot](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml/badge.svg)](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

[🌐 下载](https://xyzs996.github.io/free-proxy-health-list/zh/) · [⚡ Pro API](https://xyzs996.github.io/free-proxy-health-list/zh/api.html) · [📊 跑一个 AI agent 要花多少钱?](https://github.com/xyzs996/llm-api-pricing/blob/main/README_CN.md) · [💬 你要哪个国家的?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_CN.md) · [🐞 Issues](https://github.com/xyzs996/free-proxy-health-list/issues)

[English](./README.md) · **中文** · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md) · [Русский](./README_RU.md) · [Türkçe](./README_TR.md) · [Bahasa Indonesia](./README_ID.md) · [Tiếng Việt](./README_VI.md)

</div>

> 公开快照 · 每 30 分钟更新 · 无需注册

## 💡 为什么做这个项目？

之前我在写一个比价爬虫，单 IP 跑几次就被限流，于是去找免费代理。找到的列表都是同一个故事：一半条目是死的，标着"每日更新"的其实几个月没动过，而真正能用的那些网站，还没让我试用就先要信用卡。

我本来就为自己的爬虫跑自动健康检测，于是干脆把结果公开出来 —— 一个**真正验证过**的免费代理列表，每 30 分钟重新检测，从稳定的 CDN 链接直接拉取。不用注册，不用信用卡，没有后台。就这么简单。如果它帮你省下我当初浪费的那个下午，点个星能让下一个开发者更容易找到它。数据本身永远免费。

## 🚀 复制即用

每种格式一条命令，路径长期稳定不变。

```shell
# 全部代理
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt -o proxies.txt

# SOCKS5
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt -o socks5.txt
```

## 📦 下载文件

| 列表 | 代理数 | TXT | JSON | CSV | CDN |
| --- | --- | --- | --- | --- | --- |
| **全部代理** | `4,196` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) |
| HTTP | `1,090` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/http.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) |
| HTTPS | `1,587` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/https.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) |
| SOCKS4 | `930` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks4.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) |
| SOCKS5 | `589` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) |
| 快速代理 | `790` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) |
| 稳定代理 | `1,550` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/stability/stable/data.txt) |
| 高匿代理 | `2,998` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/anonymity/elite/data.txt) |

**按国家浏览:** [Indonesia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/id/data.txt), [United States](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/us/data.txt), [China](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/cn/data.txt), [India](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/in/data.txt), [Bangladesh](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/bd/data.txt), [Philippines](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ph/data.txt), [Mexico](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/mx/data.txt), [Brazil](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/br/data.txt), [Colombia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/co/data.txt), [Vietnam](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/vn/data.txt), [Germany](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/de/data.txt), [Russia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ru/data.txt), [Thailand](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/th/data.txt), [Canada](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ca/data.txt), [Hong Kong](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/hk/data.txt), [Venezuela](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ve/data.txt), [France](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/fr/data.txt), [Japan](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/jp/data.txt), [Singapore](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/sg/data.txt), [Netherlands](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/nl/data.txt), [Ecuador](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ec/data.txt), [Italy](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/it/data.txt), [Cambodia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/kh/data.txt), [Spain](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/es/data.txt) — [查看全部](https://github.com/xyzs996/free-proxy-health-list/tree/main/proxies/countries)

## 📊 实测可用率

几乎所有代理列表都声称"已验证"，但没有一家公开具体数字。这个项目公开：从已发布列表中随机抽样，通过每个代理端到端请求第三方 URL，结果随数据一起发布。

<img src="./assets/reliability-chart.png" width="640" alt="实测可用率">

| 列表 | 抽样可用率 |
| --- | --- |
| **最近一次抽样** | **40%** (抽样 400 个) |

<sub>方法：随机抽样，通过代理端到端请求，8 秒超时 — `http://api.ipify.org/, http://icanhazip.com/, https://api.ipify.org/, https://icanhazip.com/`</sub>

## 🧭 使用场景教程

- **[网页采集代理](https://xyzs996.github.io/free-proxy-health-list/zh/use-cases/proxy-for-web-scraping.html)** — 轮换 IP 以规避频率限制和封禁。
- **[Python requests 代理](https://xyzs996.github.io/free-proxy-health-list/zh/use-cases/python-requests-proxy.html)** — HTTP 与 SOCKS5 示例，含重试处理。
- **[搭建轮换代理池](https://xyzs996.github.io/free-proxy-health-list/zh/use-cases/rotating-proxy.html)** — 约 20 行代码实现可用的轮换逻辑。
- **[Scrapy 代理中间件](https://xyzs996.github.io/free-proxy-health-list/zh/use-cases/proxy-for-scrapy.html)** — 失败时自动轮换的即插即用中间件。
- **[curl 代理参数](https://xyzs996.github.io/free-proxy-health-list/zh/use-cases/proxy-for-curl.html)** — HTTP、HTTPS 和 SOCKS 参数及实际命令。

## 🌐 按协议浏览

- [HTTP](https://xyzs996.github.io/free-proxy-health-list/zh/protocols/http.html) — 网页请求最简单的选择，所有 HTTP 客户端都支持。
- [HTTPS](https://xyzs996.github.io/free-proxy-health-list/zh/protocols/https.html) — 已验证可通过 CONNECT 建立 TLS 隧道的 HTTP 代理。
- [SOCKS4](https://xyzs996.github.io/free-proxy-health-list/zh/protocols/socks4.html) — 轻量的传统 TCP 隧道协议。
- [SOCKS5](https://xyzs996.github.io/free-proxy-health-list/zh/protocols/socks5.html) — 支持任意 TCP 流量，另有 UDP 和远程 DNS。

## 🧱 数据结构

`data.txt` 每行一个 `host:port`。`data.json` 附带每个条目背后的健康元数据：

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

用程序读这份数据？[`llms.txt`](https://xyzs996.github.io/free-proxy-health-list/llms.txt) 一次请求就是整份快照 —— 每个列表的条数、下载地址和检测日期都在里面。

## 🔗 相关项目

同一个维护者,同一个想法 —— 不用注册就能读的公开数据:

- **[Free LLM API list](https://github.com/xyzs996/free-llm-api)** — 长期免费额度,每一条公布的限额都链到官方出处。
- **[LLM API pricing list](https://github.com/xyzs996/llm-api-pricing/blob/main/README_CN.md)** — AI 编程 Agent 到底要花多少钱。文章里引用过的每个数都在[同一张表](https://xyzs996.github.io/llm-api-pricing/figures.html)里,每行都带着它出处的整句话 ([JSON](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.json) / [CSV](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.csv))。可以先读[账单到底花在哪儿](https://xyzs996.github.io/llm-api-pricing/topics/token-optimization.html)。

## ❓ 常见问题

<details>
<summary><strong>这些免费代理安全吗？</strong></summary>

免费公共代理由不明运营者提供且被多人共享，切勿通过它们发送密码、令牌或个人数据。它们适合用于测试、采集公开页面和自动化任务，不适合承载敏感流量。
</details>

<details>
<summary><strong>列表多久更新一次？</strong></summary>

每 30 分钟重新检测并重新发布一次。每条 JSON 记录都带有 lastChecked 时间戳和延迟值，你可以自行剔除过期或过慢的条目。
</details>

<details>
<summary><strong>这里说的「已验证」具体指什么？</strong></summary>

每个条目在发布前都完成了符合协议规范的握手，并端到端转发了一次真实请求。仅能通过 TCP 连接的条目不会被发布。
</details>

<details>
<summary><strong>为什么有些代理几分钟后就失效了？</strong></summary>

免费代理本身就是易变的，随时出现也随时消失。这正是列表每 30 分钟重新检测、并按最快优先排序的原因。请务必在失败时自动切换到下一个条目。
</details>

<details>
<summary><strong>我该用哪种代理类型？</strong></summary>

HTTP 最适合普通网页请求；SOCKS5 支持任意 TCP 流量，另有 UDP 和远程 DNS；SOCKS4 是更轻量的传统备选；HTTPS 条目是已验证可隧道传输 TLS 的 HTTP 代理。
</details>

<details>
<summary><strong>需要注册或给仓库点星吗？</strong></summary>

不需要。列表是完全公开的快照，URL 稳定，无需账号也无需信用卡。点星只是帮助更多开发者发现它。
</details>

## 🧾 答得长的那几条,数都在里面

上面那些答得短,是有意的。下面这些不是 —— 每条先给一句直接的回答,再把背后每一个量出来的数摆出来,连样本量和量的时间一起:

- [How many free proxies actually work? Here is the measured rate, by protocol.](https://github.com/xyzs996/free-proxy-health-list/discussions/2) — the measured end-to-end success rate of a random sample, broken out by protocol, with the method and the timeout it was measured under.
- [Where do I get a free proxy list by country, and how many are in each?](https://github.com/xyzs996/free-proxy-health-list/discussions/3) — the per-country file path, how many entries each country has in the current snapshot, and how thin the tail gets.
- [How do I check whether a free proxy actually works?](https://github.com/xyzs996/free-proxy-health-list/discussions/4) — a working checker in ten lines, plus the four ways a naive check calls a dead proxy alive.

## ⚡ 需要生产级可靠性？

GitHub 上的列表是免费公开快照，不提供 SLA。Pro API 提供更高频的检测、按协议/国家/延迟筛选、轮换端点以及用量监控。

[申请抢先体验](https://xyzs996.github.io/free-proxy-health-list/zh/api.html)

## ⚖️ 公开快照的使用边界

免费公共代理由不明身份的第三方运营且被多人共享，切勿通过它们传输密码、令牌或个人数据。请遵守 GitHub 可接受使用政策：不得用于垃圾信息、攻击、绕过访问控制，或违反网站政策的采集行为。

## 🤝 Contributing

欢迎为文档、示例和数据易用性做贡献。参见 [CONTRIBUTING.md](./CONTRIBUTING.md)

不用出处、不用截图、也不用提 PR —— [你要的是哪个国家的?这张表里有吗?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_CN.md)

## 📄 License

[MIT](./LICENSE)
