<!-- proxyhealthlist:generated — rebuilt by `proxyhealthlist build-site` from the published
     snapshot. Hand edits are overwritten on the next run; change the
     generator (proxyhealthlist/site/) or open an issue instead. -->
<div align="center">

<a href="https://xyzs996.github.io/free-proxy-health-list/ja/"><img src="./assets/og-image.png" alt="無料プロキシリスト — 検証済み HTTP・HTTPS・SOCKS4・SOCKS5 プロキシ" width="100%"></a>

# Free Proxy Health List

**本当に検証されている無料プロキシリスト。**

[![total](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/total.json) [![http](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/http.json) [![socks5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/socks5.json) [![updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/updated.json) [![reliability](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Freliability.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/reliability.json)
[![Validate snapshot](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml/badge.svg)](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

[🌐 ダウンロード](https://xyzs996.github.io/free-proxy-health-list/ja/) · [⚡ Pro API](https://xyzs996.github.io/free-proxy-health-list/ja/api.html) · [📊 AI エージェントの運用費はいくら?](https://github.com/xyzs996/llm-api-pricing/blob/main/README_JA.md) · [💬 どの国が必要ですか?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_JA.md) · [🐞 Issues](https://github.com/xyzs996/free-proxy-health-list/issues)

[English](./README.md) · [中文](./README_CN.md) · **日本語** · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md) · [Русский](./README_RU.md) · [Türkçe](./README_TR.md) · [Bahasa Indonesia](./README_ID.md) · [Tiếng Việt](./README_VI.md)

</div>

> 公開スナップショット · 30 分ごとに更新 · 登録不要

## 💡 このプロジェクトについて

以前、価格追跡のスクレイパーを作っていたとき、単一 IP ではすぐにレート制限にかかるので無料プロキシを探しました。どのリストも同じで、半分は死んでいて、「毎日更新」と書かれたものは何か月も止まったまま。動くプロキシがあるサイトは、試す前にクレジットカードを求めてきました。

自分のスクレイピング用に自動ヘルスチェックはすでに動かしていたので、その結果を公開することにしました — **本当に検証された**無料プロキシリスト、30 分ごとに再チェックし、安定した CDN リンクから取得できます。登録もクレジットカードもダッシュボードも不要です。それだけのものです。あの日の午後を節約できたなら、スターが次の開発者の助けになります。データはどちらにせよ無料です。

## 🚀 コピーして使う

形式ごとに 1 コマンド。パスは変わりません。

```shell
# すべてのプロキシ
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt -o proxies.txt

# SOCKS5
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt -o socks5.txt
```

## 📦 ファイルをダウンロード

| リスト | 件数 | TXT | JSON | CSV | CDN |
| --- | --- | --- | --- | --- | --- |
| **すべてのプロキシ** | `4,196` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) |
| HTTP | `1,090` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/http.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) |
| HTTPS | `1,587` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/https.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) |
| SOCKS4 | `930` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks4.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) |
| SOCKS5 | `589` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) |
| 高速プロキシ | `790` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) |
| 安定プロキシ | `1,550` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/stability/stable/data.txt) |
| エリートプロキシ | `2,998` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/anonymity/elite/data.txt) |

**国別:** [Indonesia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/id/data.txt), [United States](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/us/data.txt), [China](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/cn/data.txt), [India](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/in/data.txt), [Bangladesh](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/bd/data.txt), [Philippines](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ph/data.txt), [Mexico](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/mx/data.txt), [Brazil](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/br/data.txt), [Colombia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/co/data.txt), [Vietnam](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/vn/data.txt), [Germany](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/de/data.txt), [Russia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ru/data.txt), [Thailand](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/th/data.txt), [Canada](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ca/data.txt), [Hong Kong](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/hk/data.txt), [Venezuela](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ve/data.txt), [France](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/fr/data.txt), [Japan](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/jp/data.txt), [Singapore](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/sg/data.txt), [Netherlands](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/nl/data.txt), [Ecuador](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ec/data.txt), [Italy](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/it/data.txt), [Cambodia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/kh/data.txt), [Spain](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/es/data.txt) — [すべて見る](https://github.com/xyzs996/free-proxy-health-list/tree/main/proxies/countries)

## 📊 実測稼働率

ほとんどのプロキシリストは「検証済み」と謳いますが、数値を公開するところはありません。このプロジェクトは公開します。公開リストから無作為抽出し、各プロキシ経由でサードパーティ URL をエンドツーエンドで取得した結果をデータと一緒に配信します。

<img src="./assets/reliability-chart.png" width="640" alt="実測稼働率">

| リスト | サンプル稼働率 |
| --- | --- |
| **直近のサンプル** | **40%** (400 件を抽出) |

<sub>方法：無作為抽出、プロキシ経由のエンドツーエンド取得、8 秒タイムアウト — `http://api.ipify.org/, http://icanhazip.com/, https://api.ipify.org/, https://icanhazip.com/`</sub>

## 🧭 ユースケース別ガイド

- **[スクレイピング用プロキシ](https://xyzs996.github.io/free-proxy-health-list/ja/use-cases/proxy-for-web-scraping.html)** — IP を巡回させてレート制限やBANを回避。
- **[Python requests のプロキシ設定](https://xyzs996.github.io/free-proxy-health-list/ja/use-cases/python-requests-proxy.html)** — HTTP と SOCKS5 の例、リトライ付き。
- **[ローテーティングプロキシの構築](https://xyzs996.github.io/free-proxy-health-list/ja/use-cases/rotating-proxy.html)** — 約 20 行で動くローテーション処理。
- **[Scrapy プロキシミドルウェア](https://xyzs996.github.io/free-proxy-health-list/ja/use-cases/proxy-for-scrapy.html)** — 失敗時に切り替えるミドルウェア。
- **[curl のプロキシオプション](https://xyzs996.github.io/free-proxy-health-list/ja/use-cases/proxy-for-curl.html)** — HTTP・HTTPS・SOCKS の実用コマンド。

## 🌐 プロトコル別

- [HTTP](https://xyzs996.github.io/free-proxy-health-list/ja/protocols/http.html) — 通常の Web リクエストに最適。あらゆる HTTP クライアントで使えます。
- [HTTPS](https://xyzs996.github.io/free-proxy-health-list/ja/protocols/https.html) — CONNECT で TLS をトンネルできることを検証済みの HTTP プロキシ。
- [SOCKS4](https://xyzs996.github.io/free-proxy-health-list/ja/protocols/socks4.html) — 生の TCP を中継する軽量なレガシートンネル。
- [SOCKS5](https://xyzs996.github.io/free-proxy-health-list/ja/protocols/socks5.html) — 任意の TCP に加え UDP とリモート DNS に対応。

## 🧱 データ形式

`data.txt` は 1 行に `host:port` を 1 件。`data.json` には各項目のヘルスメタデータが入ります：

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

プログラムから読みますか？[`llms.txt`](https://xyzs996.github.io/free-proxy-health-list/llms.txt) はスナップショット全体を 1 リクエストで返します — 各リストの件数、ダウンロード URL、検査日を含みます。

## 🔗 関連プロジェクト

同じメンテナー、同じ考え方 — アカウントなしで読める公開データ:

- **[Free LLM API list](https://github.com/xyzs996/free-llm-api)** — 恒久的な無料枠。公開されている上限はすべて公式の出典にリンクしています。
- **[LLM API pricing list](https://github.com/xyzs996/llm-api-pricing/blob/main/README_JA.md)** — AI コーディングエージェントの実際のコスト。記事で引用したすべての数値を[1 つの表](https://xyzs996.github.io/llm-api-pricing/figures.html)に、各行にその出典の文を添えて ([JSON](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.json) / [CSV](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.csv))。まずは[トークン料金が実際どこへ消えるのか](https://xyzs996.github.io/llm-api-pricing/topics/token-optimization.html)から。

## ❓ よくある質問

<details>
<summary><strong>この無料プロキシは安全ですか？</strong></summary>

無料の公開プロキシは運営者が不明で共有されているため、パスワードやトークン、個人情報を通さないでください。テストや公開ページの収集、自動化には使えますが、機微な通信には向きません。
</details>

<details>
<summary><strong>リストはどのくらいの頻度で更新されますか？</strong></summary>

30 分ごとに再チェックして再公開しています。各 JSON レコードには lastChecked とレイテンシが含まれるため、古い項目や遅い項目は自分で除外できます。
</details>

<details>
<summary><strong>ここでいう「検証済み」とは？</strong></summary>

公開前に、プロトコルに沿ったハンドシェイクを完了し、実際のリクエストをエンドツーエンドで中継できたものだけを掲載しています。TCP 接続が通っただけのものは公開しません。
</details>

<details>
<summary><strong>なぜ数分で使えなくなるプロキシがあるのですか？</strong></summary>

無料プロキシは本質的に不安定で、常に現れては消えます。だからこそ 30 分ごとに再チェックし、速い順に並べています。失敗したら次の項目に進む実装にしてください。
</details>

<details>
<summary><strong>どのプロキシタイプを使うべきですか？</strong></summary>

Web リクエストなら HTTP が最も簡単です。SOCKS5 は任意の TCP に加え UDP とリモート DNS に対応します。SOCKS4 は軽量なレガシー用。HTTPS は TLS をトンネルできると検証された HTTP プロキシです。
</details>

<details>
<summary><strong>登録やスターは必要ですか？</strong></summary>

不要です。安定した URL で公開されているスナップショットで、アカウントもクレジットカードも要りません。スターは他の開発者が見つけやすくなるだけです。
</details>

## 🧾 数字ごと長く答えたもの

上の回答は意図的に短くしてあります。以下は違います。まず結論を一文で示し、その裏づけとなる計測値を、サンプル数と計測時刻も添えてすべて並べています:

- [How many free proxies actually work? Here is the measured rate, by protocol.](https://github.com/xyzs996/free-proxy-health-list/discussions/2) — the measured end-to-end success rate of a random sample, broken out by protocol, with the method and the timeout it was measured under.
- [Where do I get a free proxy list by country, and how many are in each?](https://github.com/xyzs996/free-proxy-health-list/discussions/3) — the per-country file path, how many entries each country has in the current snapshot, and how thin the tail gets.
- [How do I check whether a free proxy actually works?](https://github.com/xyzs996/free-proxy-health-list/discussions/4) — a working checker in ten lines, plus the four ways a naive check calls a dead proxy alive.

## ⚡ 本番運用の信頼性が必要ですか？

GitHub のリストは SLA のない無料の公開スナップショットです。Pro API では、より新しいチェック、プロトコル・国・レイテンシによる絞り込み、ローテーションエンドポイント、利用状況の監視を提供します。

[先行アクセスに申し込む](https://xyzs996.github.io/free-proxy-health-list/ja/api.html)

## ⚖️ 公開スナップショットの利用範囲

無料の公開プロキシは不特定の第三者が運用し共有されています。パスワードやトークン、個人情報を送信しないでください。GitHub の利用規定に従い、スパム、攻撃、アクセス制御の回避、サイトポリシーに反する収集には使用しないでください。

## 🤝 Contributing

ドキュメント、サンプル、データの使いやすさへの貢献を歓迎します。参照： [CONTRIBUTING.md](./CONTRIBUTING.md)

出典もスクリーンショットも PR も要りません — [必要だったのはどの国で、このリストにありましたか?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_JA.md)

## 📄 License

[MIT](./LICENSE)
