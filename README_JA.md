# Free Proxy Health List

開発者向けの検証済み無料プロキシ一覧。**HTTP**、**SOCKS4**、**SOCKS5** プロキシを
**TXT**、**JSON**、**CSV** で、登録不要でダウンロードできます。

[![Proxies](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](./stats/latest.json)
[![HTTP](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](./proxies/protocols/http/data.txt)
[![SOCKS4](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fsocks4.json&style=for-the-badge)](./proxies/protocols/socks4/data.txt)
[![SOCKS5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](./proxies/protocols/socks5/data.txt)
[![Updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list%40main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](./stats/latest.json)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

> 公開スナップショットは常に無料。登録不要、クレジットカード不要。Star は任意で、必須ではありません。

[Website](https://xyzs996.github.io/free-proxy-health-list/) |
[Pro API Early Access](https://xyzs996.github.io/free-proxy-health-list/api.html)

**言語:** [English](./README.md) · [中文](./README_CN.md) · 日本語 · [한국어](./README_KO.md)

## このプロジェクトについて

以前、副業で価格追跡用の小さなスクレイパーを作っていました。単一の IP から実行するたびに
レート制限に引っかかるので、無料プロキシを探しました。しかしどの一覧も同じで、半分は
すでに死んでいて、「毎日更新」と書かれているものも数か月動いておらず、まともに動く
プロキシを提供するサイトは、試す前にクレジットカードを要求してきました。

自分のスクレイピング用にすでに自動ヘルスチェックを回していたので、その結果を公開する
ことにしました。**本当に検証された無料プロキシ一覧**を、1 時間ごとに再チェックし、
安定した CDN 直リンクから取得できる形で。登録不要、クレジットカード不要、管理画面なし。

それだけのプロジェクトです。もし私が失ったあの午後を節約できたなら、Star は次の開発者が
見つけやすくしてくれます。データはいずれにせよ無料です。

## クイックスタート

すべてのプロキシをダウンロード:

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt -o proxies.txt
```

SOCKS5 のみをダウンロード:

```shell
curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt -o socks5.txt
```

最初の HTTP プロキシを curl で使う:

```shell
proxy="$(curl -sL https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt | head -n 1)"
curl -x "http://$proxy" -I "http://example.com/" --max-time 10
```

## ダウンロードファイル

| 種類 | TXT | JSON | CSV |
| --- | --- | --- | --- |
| すべてのプロキシ | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.csv) |
| HTTP | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.csv) |
| HTTPS | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.csv) |
| SOCKS4 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.csv) |
| SOCKS5 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.csv) |
| 高速プロキシ | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.csv) |
| Top 1000 | [TXT](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.txt) | [JSON](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.json) | [CSV](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/quality/top-1000/data.csv) |

## 開発者に選ばれる理由

- スクリプト、クローラー、自動化ツールから直接使える CDN リンク。
- TXT、JSON、CSV の安定したパス。
- 公開ヘルスメタデータ: プロトコル、レイテンシ、品質スコア、チェック方式、更新時刻。
- 公開スナップショットはアカウント不要。
- より新鮮なチェック・フィルタリング・ローテーションが必要な場合の別途プロダクション経路。

役に立ったら、Star は他の開発者が見つける助けになります。データは Star なしでも無料で使えます。

## 用途

開発者がこの無料プロキシ一覧を使う代表的な方法。各ガイドにコピペ可能なコードがあります:

- **[Web スクレイピング](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-web-scraping.html)** — IP をローテーションしてレート制限や BAN を回避。
- **[Python `requests`](https://xyzs996.github.io/free-proxy-health-list/use-cases/python-requests-proxy.html)** — HTTP と SOCKS5 のプロキシ例。
- **[ローテーションプロキシプール](https://xyzs996.github.io/free-proxy-health-list/use-cases/rotating-proxy.html)** — 無料で自分だけの rotating proxy を構築。
- **[Scrapy](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-scrapy.html)** — ローテーション用ミドルウェア。
- **[curl](https://xyzs996.github.io/free-proxy-health-list/use-cases/proxy-for-curl.html)** — HTTP・HTTPS・SOCKS のプロキシオプション。

## プロトコル別に見る

ダウンロードリンク、コード、リアルタイム件数を掲載した専用ページ:

- [無料 HTTP プロキシ一覧](https://xyzs996.github.io/free-proxy-health-list/protocols/http.html)
- [無料 HTTPS プロキシ一覧](https://xyzs996.github.io/free-proxy-health-list/protocols/https.html)
- [無料 SOCKS4 プロキシ一覧](https://xyzs996.github.io/free-proxy-health-list/protocols/socks4.html)
- [無料 SOCKS5 プロキシ一覧](https://xyzs996.github.io/free-proxy-health-list/protocols/socks5.html)

## データ形式

`data.txt` は 1 行につき 1 つの `host:port` を含みます。`data.json` はより詳細なレコードを含みます:

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

## サンプル

- [curl](./examples/curl/examples.sh)
- [Python requests](./examples/python/requests_example.py)
- [Node.js fetch](./examples/nodejs/fetch-example.mjs)
- [Playwright](./examples/playwright/playwright-example.py)
- [Scrapy](./examples/scrapy/settings.py)

## Pro API Early Access

GitHub の一覧は SLA のない無料の公開スナップショットです。プロダクション用途には、より
新鮮なチェック、フィルタリング、ローテーションエンドポイント、上限緩和、使用量モニタリングを
備えた Pro API を計画しています。

[Pro API early access に参加](https://xyzs996.github.io/free-proxy-health-list/api.html)

## よくある質問

**これらの無料プロキシは安全に使えますか？**
公開の無料プロキシは共有され、運営者が不明です。パスワード・トークン・個人情報を通しては
いけません。テスト、公開ページのスクレイピング、自動化に使い、機微な通信には使わないでください。

**一覧はどのくらいの頻度で更新されますか？**
各プロキシは再チェックされ、一覧は 1 時間ごとに再公開されます。各 JSON レコードには
`lastChecked` のタイムスタンプと `latencyMs` の値が含まれ、古い・遅いエントリを除外できます。

**なぜ数分で使えなくなるプロキシがあるのですか？**
無料プロキシは本質的に不安定で、常に現れては消えます。だからこそ一覧は 1 時間ごとに
ヘルスチェックされ、速い順に並べられています。失敗したら次のエントリへ回してください。

**どのプロキシタイプを使うべきですか？**
Web リクエストには HTTP が最も簡単です。[SOCKS5](https://xyzs996.github.io/free-proxy-health-list/protocols/socks5.html)
は任意の TCP 通信に加え UDP とリモート DNS に対応します。SOCKS4 はより軽量な旧来の
選択肢です。HTTPS のエントリは TLS トンネルが検証済みの HTTP プロキシです。

**登録や Star は必要ですか？**
いいえ。一覧は安定した CDN リンク上の完全に公開されたスナップショットで、アカウントも
クレジットカードも不要です。Star は他の開発者が見つける助けになるだけです。

## 責任ある利用

[GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies) に従ってください。
本プロジェクトを、スパム、サービスへの攻撃、アクセス制御の回避、アカウントの大量登録、
サイトポリシーに反するスクレイピング、その他の違法行為に使用しないでください。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=xyzs996/free-proxy-health-list&type=Date)](https://www.star-history.com/#xyzs996/free-proxy-health-list&Date)

## コントリビュート

ドキュメント、サンプル、公開データの使いやすさへの貢献を歓迎します。
[CONTRIBUTING.md](./CONTRIBUTING.md) を参照してください。
