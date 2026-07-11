# Free Proxy Health List

面向开发者的免费代理健康快照。无需注册即可下载 **HTTP**、**SOCKS4**、**SOCKS5** 代理，支持 **TXT**、**JSON**、**CSV**。

[![Proxies](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](./stats/latest.json)
[![HTTP](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](./proxies/protocols/http/data.txt)
[![SOCKS4](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fsocks4.json&style=for-the-badge)](./proxies/protocols/socks4/data.txt)
[![SOCKS5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](./proxies/protocols/socks5/data.txt)
[![Updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](./stats/latest.json)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

> 公开快照永久免费，不需要注册，也不需要 Star 才能使用。Star 只是可选支持。

[Website](https://xyzs996.github.io/free-proxy-health-list/) |
[Pro API Early Access](https://xyzs996.github.io/free-proxy-health-list/api.html) |
[English](./README.md)

## 为什么做这个项目？

前段时间我在业余时间写一个比价爬虫。单个 IP 跑几次就被限流，于是去找免费代理。
结果每个列表都是同一个套路：一半的条目早就失效，号称"每日更新"的其实几个月没动过，
而真正能用的那些站点，还没让你测试就先要绑信用卡。

我本来就为自己的爬虫跑自动健康检测，于是干脆把结果公开出来——一个**真正经过验证、
每小时重新检测**、可以从稳定 CDN 直链拉取的免费代理列表。无需注册、无需信用卡、
没有后台。

就这么简单。如果它帮你省下了我当初浪费的那个下午，Star 能让下一个开发者更快找到它；
但数据本身永远免费，不需要 Star。

## 快速开始

下载全部代理：

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt -o proxies.txt
```

只下载 SOCKS5：

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt -o socks5.txt
```

用第一个 HTTP 代理测试 curl：

```shell
proxy="$(curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt | head -n 1)"
curl -x "http://$proxy" -I "http://example.com/" --max-time 10
```

## 下载文件

| 类型 | TXT | JSON | CSV |
| --- | --- | --- | --- |
| 全部代理 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.csv) |
| HTTP | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.csv) |
| HTTPS | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.csv) |
| SOCKS4 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.csv) |
| SOCKS5 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.csv) |
| 快速代理 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.csv) |
| Top 1000 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.csv) |

## 为什么适合开发者

- CDN 直链，脚本、爬虫、自动化工具都能直接消费。
- TXT、JSON、CSV 路径稳定。
- 公开健康信息：协议、延迟、质量分、检测方式、更新时间。
- 免费快照无需账号。
- 需要更高稳定性时，有独立的 Pro API 升级路径。

如果这个项目节省了你的时间，Star 可以帮助更多开发者发现它；但数据不要求 Star 才能使用。

## 用它来做什么

开发者常见的用法，每个指南都有可复制的代码：

- **[网页爬虫抓取](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-web-scraping.html)** —— 轮换 IP，规避限流和封禁。
- **[Python `requests`](https://xyzs996.github.io/free-proxy-health-list/use-cases/python-requests-proxy.html)** —— HTTP 与 SOCKS5 代理示例。
- **[轮换代理池](https://xyzs996.github.io/free-proxy-health-list/use-cases/rotating-proxy.html)** —— 免费搭一个自己的 rotating proxy。
- **[Scrapy](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-scrapy.html)** —— 轮换代理中间件。
- **[curl](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-curl.html)** —— HTTP、HTTPS、SOCKS 代理参数。

## 按协议浏览

各协议独立页面，含下载链接、代码和实时数量：

- [免费 HTTP 代理列表](https://xyzs996.github.io/free-proxy-health-list/protocols/http.html)
- [免费 HTTPS 代理列表](https://xyzs996.github.io/free-proxy-health-list/protocols/https.html)
- [免费 SOCKS4 代理列表](https://xyzs996.github.io/free-proxy-health-list/protocols/socks4.html)
- [免费 SOCKS5 代理列表](https://xyzs996.github.io/free-proxy-health-list/protocols/socks5.html)

## Pro API Early Access

GitHub 仓库是免费公开快照，没有 SLA。生产场景可以关注后续 Pro API：更实时的检测、筛选、轮换端点、更高限制和用量监控。

[加入 Pro API early access](https://xyzs996.github.io/free-proxy-health-list/api.html)

## 常见问题

**这些免费代理安全吗？**
公开免费代理是共享的、由未知运营方提供，所以永远不要通过它们传输密码、令牌或个人数据。
它们适合测试、抓取公开页面和自动化，不适合敏感流量。

**列表多久更新一次？**
每个代理都会被重新检测，列表按每小时的节奏重新发布。每条 JSON 记录都带
`lastChecked` 时间戳和 `latencyMs` 延迟，方便你剔除过期或过慢的条目。

**为什么有些代理几分钟就失效了？**
免费代理天生就不稳定——不断有新的出现、旧的消失。这正是列表每小时做健康检测、
并按速度从快到慢排序的原因。失败时请循环取下一个。

**该用哪种协议？**
HTTP 最简单，适合网页请求。[SOCKS5](https://xyzs996.github.io/free-proxy-health-list/protocols/socks5.html)
支持任意 TCP 流量以及 UDP 和远程 DNS。SOCKS4 是更轻量的老协议备选。HTTPS 条目是
经过验证能隧道 TLS 的 HTTP 代理。

**需要注册或 Star 吗？**
不需要。列表是完全公开的快照，走稳定 CDN 直链，无账号、无信用卡。Star 只是帮助
其他开发者发现它。

## 合规使用

请遵守 [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)。不要将本项目用于垃圾请求、攻击服务、绕过访问控制、批量注册账号、违反网站政策的抓取或任何违法用途。
