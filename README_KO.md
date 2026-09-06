<!-- proxyhealthlist:generated — rebuilt by `proxyhealthlist build-site` from the published
     snapshot. Hand edits are overwritten on the next run; change the
     generator (proxyhealthlist/site/) or open an issue instead. -->
<div align="center">

<a href="https://xyzs996.github.io/free-proxy-health-list/ko/"><img src="./assets/og-image.png" alt="무료 프록시 목록 — 검증된 HTTP, HTTPS, SOCKS4, SOCKS5 프록시" width="100%"></a>

# Free Proxy Health List

**실제로 검증된 무료 프록시 목록.**

[![total](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/total.json) [![http](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/http.json) [![socks5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/socks5.json) [![updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/updated.json) [![reliability](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Freliability.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/reliability.json)
[![Validate snapshot](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml/badge.svg)](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

[🌐 다운로드](https://xyzs996.github.io/free-proxy-health-list/ko/) · [⚡ Pro API](https://xyzs996.github.io/free-proxy-health-list/ko/api.html) · [📊 AI 에이전트 굴리는 데 얼마 드나?](https://github.com/xyzs996/llm-api-pricing/blob/main/README_KO.md) · [💬 어느 나라가 필요한가요?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_KO.md) · [🐞 Issues](https://github.com/xyzs996/free-proxy-health-list/issues)

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · **한국어** · [Español](./README_ES.md) · [Português](./README_PT.md) · [Русский](./README_RU.md) · [Türkçe](./README_TR.md) · [Bahasa Indonesia](./README_ID.md) · [Tiếng Việt](./README_VI.md)

</div>

> 공개 스냅샷 · 30분마다 갱신 · 가입 불필요

## 💡 이 프로젝트를 만든 이유

얼마 전 가격 추적 스크레이퍼를 만들다가 단일 IP로는 매번 요청 제한에 걸려 무료 프록시를 찾아다녔습니다. 어느 목록이나 사정은 같았습니다. 절반은 죽어 있고, "매일 갱신"이라 적힌 것들은 몇 달째 그대로였으며, 실제로 작동하는 프록시가 있는 사이트는 시험해 보기도 전에 신용카드를 요구했습니다.

제 스크래핑을 위해 이미 자동 상태 검사를 돌리고 있었기에 그 결과를 공개하기 시작했습니다 — **실제로 검증된** 무료 프록시 목록, 30분마다 재검사, 안정적인 CDN 링크에서 바로 받기. 가입도 카드도 대시보드도 없습니다. 그게 전부입니다. 제가 날린 그 오후를 아껴 준다면, 스타가 다음 개발자에게 도움이 됩니다. 데이터는 어느 쪽이든 무료입니다.

## 🚀 복사해서 사용

형식마다 명령 하나. 경로는 변하지 않습니다.

```shell
# 전체 프록시
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt -o proxies.txt

# SOCKS5
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt -o socks5.txt
```

## 📦 파일 다운로드

| 목록 | 개수 | TXT | JSON | CSV | CDN |
| --- | --- | --- | --- | --- | --- |
| **전체 프록시** | `4,196` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) |
| HTTP | `1,090` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/http.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) |
| HTTPS | `1,587` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/https.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) |
| SOCKS4 | `930` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks4.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) |
| SOCKS5 | `589` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) |
| 빠른 프록시 | `790` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) |
| 안정 프록시 | `1,550` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/stability/stable/data.txt) |
| 엘리트 프록시 | `2,998` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/anonymity/elite/data.txt) |

**국가별 보기:** [Indonesia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/id/data.txt), [United States](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/us/data.txt), [China](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/cn/data.txt), [India](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/in/data.txt), [Bangladesh](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/bd/data.txt), [Philippines](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ph/data.txt), [Mexico](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/mx/data.txt), [Brazil](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/br/data.txt), [Colombia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/co/data.txt), [Vietnam](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/vn/data.txt), [Germany](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/de/data.txt), [Russia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ru/data.txt), [Thailand](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/th/data.txt), [Canada](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ca/data.txt), [Hong Kong](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/hk/data.txt), [Venezuela](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ve/data.txt), [France](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/fr/data.txt), [Japan](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/jp/data.txt), [Singapore](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/sg/data.txt), [Netherlands](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/nl/data.txt), [Ecuador](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ec/data.txt), [Italy](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/it/data.txt), [Cambodia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/kh/data.txt), [Spain](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/es/data.txt) — [전체 보기](https://github.com/xyzs996/free-proxy-health-list/tree/main/proxies/countries)

## 📊 실측 작동률

대부분의 프록시 목록은 검증되었다고 주장하지만 숫자를 공개하는 곳은 없습니다. 이 프로젝트는 공개합니다. 게시된 목록에서 무작위 표본을 뽑아 각 프록시를 통해 제3자 URL을 엔드투엔드로 가져온 결과를 데이터와 함께 배포합니다.

<img src="./assets/reliability-chart.png" width="640" alt="실측 작동률">

| 목록 | 표본 작동률 |
| --- | --- |
| **최근 표본** | **40%** (400개 표본) |

<sub>방법: 무작위 표본, 프록시를 통한 엔드투엔드 요청, 8초 제한 — `http://api.ipify.org/, http://icanhazip.com/, https://api.ipify.org/, https://icanhazip.com/`</sub>

## 🧭 활용 사례 가이드

- **[웹 스크래핑 프록시](https://xyzs996.github.io/free-proxy-health-list/ko/use-cases/proxy-for-web-scraping.html)** — IP를 교체해 속도 제한과 차단을 피하세요.
- **[Python requests 프록시](https://xyzs996.github.io/free-proxy-health-list/ko/use-cases/python-requests-proxy.html)** — 재시도가 포함된 HTTP·SOCKS5 예제.
- **[로테이팅 프록시 풀 만들기](https://xyzs996.github.io/free-proxy-health-list/ko/use-cases/rotating-proxy.html)** — 약 20줄로 동작하는 순환 로직.
- **[Scrapy 프록시 미들웨어](https://xyzs996.github.io/free-proxy-health-list/ko/use-cases/proxy-for-scrapy.html)** — 실패 시 교체하는 미들웨어.
- **[curl 프록시 옵션](https://xyzs996.github.io/free-proxy-health-list/ko/use-cases/proxy-for-curl.html)** — HTTP, HTTPS, SOCKS 실전 명령어.

## 🌐 프로토콜별 보기

- [HTTP](https://xyzs996.github.io/free-proxy-health-list/ko/protocols/http.html) — 웹 요청에 가장 간단하며 모든 HTTP 클라이언트에서 작동합니다.
- [HTTPS](https://xyzs996.github.io/free-proxy-health-list/ko/protocols/https.html) — CONNECT로 TLS 터널링이 검증된 HTTP 프록시.
- [SOCKS4](https://xyzs996.github.io/free-proxy-health-list/ko/protocols/socks4.html) — 원시 TCP를 중계하는 경량 레거시 터널.
- [SOCKS5](https://xyzs996.github.io/free-proxy-health-list/ko/protocols/socks5.html) — 모든 TCP 트래픽과 UDP, 원격 DNS 지원.

## 🧱 데이터 형식

`data.txt`는 한 줄에 `host:port` 하나. `data.json`은 각 항목의 상태 메타데이터를 담습니다:

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

프로그램으로 읽고 있나요? [`llms.txt`](https://xyzs996.github.io/free-proxy-health-list/llms.txt) 는 요청 한 번으로 스냅샷 전체를 줍니다 — 목록별 개수, 다운로드 주소, 검사 날짜까지.

## 🔗 관련 프로젝트

같은 관리자, 같은 취지 — 계정 없이 읽을 수 있는 공개 데이터:

- **[Free LLM API list](https://github.com/xyzs996/free-llm-api)** — 영구 무료 등급. 공개된 모든 한도는 공식 출처로 연결됩니다.
- **[LLM API pricing list](https://github.com/xyzs996/llm-api-pricing/blob/main/README_KO.md)** — AI 코딩 에이전트의 실제 비용. 글에서 인용한 모든 수치를 [한 표](https://xyzs996.github.io/llm-api-pricing/figures.html)에, 각 행마다 출처 문장을 함께 ([JSON](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.json) / [CSV](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.csv)). 먼저 [토큰 요금이 실제로 어디로 가는지](https://xyzs996.github.io/llm-api-pricing/topics/token-optimization.html)부터.

## ❓ 자주 묻는 질문

<details>
<summary><strong>이 무료 프록시는 안전한가요?</strong></summary>

무료 공개 프록시는 운영자를 알 수 없고 공유되므로 비밀번호, 토큰, 개인정보를 보내지 마세요. 테스트, 공개 페이지 수집, 자동화에는 적합하지만 민감한 트래픽에는 적합하지 않습니다.
</details>

<details>
<summary><strong>목록은 얼마나 자주 갱신되나요?</strong></summary>

30분마다 다시 검사하고 다시 게시합니다. 각 JSON 레코드에 lastChecked와 지연 값이 있어 오래되거나 느린 항목을 직접 걸러낼 수 있습니다.
</details>

<details>
<summary><strong>여기서 '검증됨'은 무슨 뜻인가요?</strong></summary>

게시 전에 프로토콜에 맞는 핸드셰이크를 마치고 실제 요청을 엔드투엔드로 중계한 항목만 싣습니다. TCP 연결만 되는 항목은 게시하지 않습니다.
</details>

<details>
<summary><strong>왜 몇 분 만에 작동하지 않는 프록시가 있나요?</strong></summary>

무료 프록시는 본질적으로 불안정해 계속 나타나고 사라집니다. 그래서 30분마다 재검사하고 빠른 순으로 정렬합니다. 실패하면 다음 항목으로 넘어가도록 구현하세요.
</details>

<details>
<summary><strong>어떤 프록시 유형을 써야 하나요?</strong></summary>

웹 요청에는 HTTP가 가장 간단합니다. SOCKS5는 모든 TCP와 UDP, 원격 DNS를 지원합니다. SOCKS4는 가벼운 레거시 대안이며, HTTPS는 TLS 터널링이 검증된 HTTP 프록시입니다.
</details>

<details>
<summary><strong>가입하거나 스타를 눌러야 하나요?</strong></summary>

아니요. 안정적인 URL의 완전 공개 스냅샷이며 계정도 카드도 필요 없습니다. 스타는 다른 개발자가 찾는 데 도움이 될 뿐입니다.
</details>

## 🧾 수치까지 길게 답한 글

위 답변은 일부러 짧게 썼습니다. 아래 글은 다릅니다. 각각 결론을 한 문장으로 먼저 밝히고, 그 근거가 된 측정값을 표본 크기와 측정 시각까지 함께 모두 보여줍니다:

- [How many free proxies actually work? Here is the measured rate, by protocol.](https://github.com/xyzs996/free-proxy-health-list/discussions/2) — the measured end-to-end success rate of a random sample, broken out by protocol, with the method and the timeout it was measured under.
- [Where do I get a free proxy list by country, and how many are in each?](https://github.com/xyzs996/free-proxy-health-list/discussions/3) — the per-country file path, how many entries each country has in the current snapshot, and how thin the tail gets.
- [How do I check whether a free proxy actually works?](https://github.com/xyzs996/free-proxy-health-list/discussions/4) — a working checker in ten lines, plus the four ways a naive check calls a dead proxy alive.

## ⚡ 운영 환경의 신뢰성이 필요하신가요?

GitHub 목록은 SLA가 없는 무료 공개 스냅샷입니다. Pro API는 더 잦은 검사, 프로토콜·국가·지연 시간 필터링, 로테이팅 엔드포인트, 사용량 모니터링을 제공합니다.

[사전 이용 신청](https://xyzs996.github.io/free-proxy-health-list/ko/api.html)

## ⚖️ 공개 스냅샷 이용 범위

무료 공개 프록시는 알 수 없는 주체가 운영하며 공유됩니다. 비밀번호, 토큰, 개인정보를 전송하지 마세요. GitHub 이용 정책에 따라 스팸, 공격, 접근 제어 우회, 사이트 정책에 어긋나는 수집에 사용하지 마세요.

## 🤝 Contributing

문서, 예제, 데이터 활용성에 대한 기여를 환영합니다. 참고: [CONTRIBUTING.md](./CONTRIBUTING.md)

출처도 스크린샷도 PR도 필요 없습니다 — [어느 나라가 필요했고, 이 목록에 있었나요?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_KO.md)

## 📄 License

[MIT](./LICENSE)
