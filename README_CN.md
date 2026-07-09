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

## Pro API Early Access

GitHub 仓库是免费公开快照，没有 SLA。生产场景可以关注后续 Pro API：更实时的检测、筛选、轮换端点、更高限制和用量监控。

[加入 Pro API early access](https://xyzs996.github.io/free-proxy-health-list/api.html)

## 合规使用

请遵守 [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)。不要将本项目用于垃圾请求、攻击服务、绕过访问控制、批量注册账号、违反网站政策的抓取或任何违法用途。
