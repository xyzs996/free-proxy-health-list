# Free Proxy List

面向开发者的免费代理列表，自动验证 **HTTP**、**HTTPS**、**SOCKS4**、**SOCKS5** 代理，输出 **JSON**、**TXT**、**CSV**，无需注册即可使用。

[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/xyzs996/free-proxy-health-list?style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/commits/main)
[![License](https://img.shields.io/github/license/xyzs996/free-proxy-health-list?style=for-the-badge)](./LICENSE)

> 最新快照见 [`stats/latest.json`](./stats/latest.json)。公开列表永久免费，Star 只是可选支持，不是使用门槛。

[English](./README.md) | [中文](./README_CN.md)

## 一键下载

仓库发布后可通过 jsDelivr 直接拉取：

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt -o proxies.txt
```

| 类型 | TXT | JSON | CSV |
| --- | --- | --- | --- |
| 全部代理 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.csv) |
| HTTP | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.csv) |
| HTTPS | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.csv) |
| SOCKS4 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.csv) |
| SOCKS5 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.csv) |
| 快速代理 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.csv) |
| Top 1000 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.csv) |

## 项目定位

这个项目不是简单堆一个 `ip:port` 列表，而是要做“可验证、可集成、可持续更新”的免费代理数据集：

- 自动采集和去重。
- 基础 TCP / HTTP / HTTPS CONNECT 验证。
- 输出延迟、质量分、验证方式、更新时间。
- 按协议、速度、质量切片。
- 免费仓库做 SEO 和开发者入口，Pro API 做稳定性和商业转化。

## 本地运行

```shell
python -m proxyhealthlist update \
  --sources sources/default_sources.txt \
  --limit 2000 \
  --workers 100 \
  --timeout 5
```

生成文件会写入 `proxies/` 和 `stats/`。

## 商业化边界

免费仓库应该一直保持真正可用，不要把免费层做成残缺诱饵。更合理的边界是：

- 免费仓库：公开快照、CDN 直链、基础质量分、无 SLA。
- Pro API：实时全量、最近 60 秒验证、国家/协议/延迟筛选、轮换端点、更高并发、监控和 SLA。

## 合规使用

请遵守 [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)。不要将本项目用于垃圾请求、攻击服务、绕过访问控制、批量注册账号、违反网站政策的抓取或任何违法用途。
