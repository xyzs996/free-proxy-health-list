# Free Proxy Health List

개발자를 위한 검증된 무료 프록시 목록. **HTTP**, **SOCKS4**, **SOCKS5** 프록시를
**TXT**, **JSON**, **CSV** 형식으로 가입 없이 다운로드하세요.

[![Proxies](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](./stats/latest.json)
[![HTTP](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](./proxies/protocols/http/data.txt)
[![SOCKS4](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fsocks4.json&style=for-the-badge)](./proxies/protocols/socks4/data.txt)
[![SOCKS5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](./proxies/protocols/socks5/data.txt)
[![Updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](./stats/latest.json)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

> 공개 스냅샷은 항상 무료입니다. 가입 불필요, 신용카드 불필요. Star는 선택 사항이며 절대 필수가 아닙니다.

[Website](https://xyzs996.github.io/free-proxy-health-list/) |
[Pro API Early Access](https://xyzs996.github.io/free-proxy-health-list/api.html)

**언어:** [English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · 한국어

## 이 프로젝트에 대하여

얼마 전 부업으로 가격 추적용 작은 스크레이퍼를 만들고 있었습니다. 하나의 IP로 실행할 때마다
속도 제한에 걸려서 무료 프록시를 찾아 나섰습니다. 그런데 모든 목록이 똑같았습니다. 절반은
이미 죽어 있었고, "매일 업데이트"라고 적힌 것도 몇 달째 그대로였으며, 제대로 작동하는
프록시를 제공하는 사이트는 테스트해 보기도 전에 신용카드를 요구했습니다.

저는 이미 제 스크레이핑을 위해 자동 상태 점검을 돌리고 있었기에, 그 결과를 공개하기로
했습니다. **실제로 검증된 무료 프록시 목록**을, 매시간 다시 점검하고, 안정적인 CDN
링크에서 바로 받을 수 있게요. 가입 불필요, 신용카드 불필요, 대시보드 없음.

그게 전부입니다. 제가 잃어버린 그 오후를 아껴 드릴 수 있다면, Star는 다음 개발자가 이걸
발견하는 데 도움이 됩니다. 데이터는 어느 쪽이든 무료입니다.

## 빠른 시작

모든 프록시 다운로드:

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt -o proxies.txt
```

SOCKS5만 다운로드:

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt -o socks5.txt
```

첫 번째 HTTP 프록시를 curl로 사용:

```shell
proxy="$(curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt | head -n 1)"
curl -x "http://$proxy" -I "http://example.com/" --max-time 10
```

## 다운로드 파일

| 종류 | TXT | JSON | CSV |
| --- | --- | --- | --- |
| 전체 프록시 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.csv) |
| HTTP | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.csv) |
| HTTPS | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.csv) |
| SOCKS4 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.csv) |
| SOCKS5 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.csv) |
| 빠른 프록시 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.csv) |
| Top 1000 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.csv) |

## 개발자가 사용하는 이유

- 스크립트, 크롤러, 자동화 도구에서 바로 쓰는 CDN 링크.
- 안정적인 TXT, JSON, CSV 경로.
- 공개 상태 메타데이터: 프로토콜, 지연 시간, 품질 점수, 점검 방식, 갱신 시각.
- 공개 스냅샷은 계정 불필요.
- 더 신선한 점검·필터링·로테이션이 필요한 경우를 위한 별도 프로덕션 경로.

시간을 아꼈다면, Star는 다른 개발자가 목록을 발견하는 데 도움이 됩니다. 데이터는 Star 없이도 무료입니다.

## 활용 사례

개발자가 이 무료 프록시 목록을 사용하는 대표적인 방법. 각 가이드에 복사해 쓸 수 있는 코드가 있습니다:

- **[웹 스크래핑](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-web-scraping.html)** — IP를 로테이션해 속도 제한과 차단을 회피.
- **[Python `requests`](https://xyzs996.github.io/free-proxy-health-list/use-cases/python-requests-proxy.html)** — HTTP 및 SOCKS5 프록시 예제.
- **[로테이션 프록시 풀](https://xyzs996.github.io/free-proxy-health-list/use-cases/rotating-proxy.html)** — 무료로 나만의 rotating proxy 구축.
- **[Scrapy](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-scrapy.html)** — 로테이션 미들웨어.
- **[curl](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-curl.html)** — HTTP·HTTPS·SOCKS 프록시 옵션.

## 프로토콜별 보기

다운로드 링크, 코드, 실시간 개수를 담은 전용 페이지:

- [무료 HTTP 프록시 목록](https://xyzs996.github.io/free-proxy-health-list/protocols/http.html)
- [무료 HTTPS 프록시 목록](https://xyzs996.github.io/free-proxy-health-list/protocols/https.html)
- [무료 SOCKS4 프록시 목록](https://xyzs996.github.io/free-proxy-health-list/protocols/socks4.html)
- [무료 SOCKS5 프록시 목록](https://xyzs996.github.io/free-proxy-health-list/protocols/socks5.html)

## 데이터 형식

`data.txt`는 한 줄에 하나의 `host:port`를 담습니다. `data.json`은 더 풍부한 레코드를 담습니다:

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

## 예제

- [curl](./examples/curl/examples.sh)
- [Python requests](./examples/python/requests_example.py)
- [Node.js fetch](./examples/nodejs/fetch-example.mjs)
- [Playwright](./examples/playwright/playwright-example.py)
- [Scrapy](./examples/scrapy/settings.py)

## Pro API Early Access

GitHub 목록은 SLA가 없는 무료 공개 스냅샷입니다. 프로덕션 용도로는 더 신선한 점검,
필터링, 로테이션 엔드포인트, 상향된 한도, 사용량 모니터링을 갖춘 Pro API를 계획하고 있습니다.

[Pro API early access 참여](https://xyzs996.github.io/free-proxy-health-list/api.html)

## 자주 묻는 질문

**이 무료 프록시는 안전한가요?**
공개 무료 프록시는 공유되며 운영자를 알 수 없습니다. 비밀번호·토큰·개인정보를 절대 통과
시키지 마세요. 테스트, 공개 페이지 스크래핑, 자동화에 사용하고 민감한 트래픽에는 쓰지 마세요.

**목록은 얼마나 자주 갱신되나요?**
각 프록시는 다시 점검되고 목록은 매시간 재게시됩니다. 각 JSON 레코드에는 `lastChecked`
타임스탬프와 `latencyMs` 값이 있어 오래되거나 느린 항목을 걸러낼 수 있습니다.

**왜 몇 분 만에 작동을 멈추는 프록시가 있나요?**
무료 프록시는 본질적으로 불안정하여 끊임없이 나타나고 사라집니다. 그래서 목록은 매시간
상태 점검되고 빠른 순으로 정렬됩니다. 실패하면 항상 다음 항목으로 넘어가세요.

**어떤 프록시 유형을 써야 하나요?**
웹 요청에는 HTTP가 가장 간단합니다. [SOCKS5](https://xyzs996.github.io/free-proxy-health-list/protocols/socks5.html)
는 임의의 TCP 트래픽과 UDP, 원격 DNS를 지원합니다. SOCKS4는 더 가벼운 레거시 대안입니다.
HTTPS 항목은 TLS 터널링이 검증된 HTTP 프록시입니다.

**가입이나 Star가 필요한가요?**
아니요. 목록은 안정적인 CDN 링크의 완전 공개 스냅샷이며 계정도 신용카드도 필요 없습니다.
Star는 다른 개발자가 발견하는 데 도움이 될 뿐입니다.

## 책임 있는 사용

[GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)를 준수하세요.
이 프로젝트를 스팸, 서비스 공격, 접근 제어 우회, 계정 대량 등록, 사이트 정책을 위반하는
스크래핑, 기타 불법 행위에 사용하지 마세요.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=xyzs996/free-proxy-health-list&type=Date)](https://www.star-history.com/#xyzs996/free-proxy-health-list&Date)

## 기여

문서, 예제, 공개 데이터 사용성에 대한 기여를 환영합니다.
[CONTRIBUTING.md](./CONTRIBUTING.md)를 참고하세요.
