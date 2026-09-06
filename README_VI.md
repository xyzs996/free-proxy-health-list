<!-- proxyhealthlist:generated — rebuilt by `proxyhealthlist build-site` from the published
     snapshot. Hand edits are overwritten on the next run; change the
     generator (proxyhealthlist/site/) or open an issue instead. -->
<div align="center">

<a href="https://xyzs996.github.io/free-proxy-health-list/vi/"><img src="./assets/og-image.png" alt="Danh sách proxy miễn phí — HTTP, HTTPS, SOCKS4 và SOCKS5 đã kiểm chứng" width="100%"></a>

# Free Proxy Health List

**Danh sách proxy miễn phí thực sự được kiểm chứng.**

[![total](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/total.json) [![http](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/http.json) [![socks5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/socks5.json) [![updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/updated.json) [![reliability](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Freliability.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/reliability.json)
[![Validate snapshot](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml/badge.svg)](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

[🌐 Tải xuống](https://xyzs996.github.io/free-proxy-health-list/vi/) · [⚡ Pro API](https://xyzs996.github.io/free-proxy-health-list/vi/api.html) · [📊 Chạy một tác nhân AI tốn bao nhiêu?](https://github.com/xyzs996/llm-api-pricing/blob/main/README_VI.md) · [💬 Bạn cần proxy ở nước nào?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_VI.md) · [🐞 Issues](https://github.com/xyzs996/free-proxy-health-list/issues)

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md) · [Русский](./README_RU.md) · [Türkçe](./README_TR.md) · [Bahasa Indonesia](./README_ID.md) · **Tiếng Việt**

</div>

> Ảnh chụp công khai · cập nhật mỗi 30 phút · không cần đăng ký

## 💡 Vì sao có dự án này?

Cách đây một thời gian tôi viết một trình thu thập dữ liệu theo dõi giá. Mỗi lần chạy đều bị giới hạn tần suất vì chỉ có một IP, nên tôi đi tìm proxy miễn phí. Danh sách nào cũng cùng một câu chuyện: một nửa số mục đã chết, những cái ghi "cập nhật hằng ngày" thì nhiều tháng không đổi, còn các trang có proxy chạy được thì đòi thẻ tín dụng trước cả khi cho tôi thử.

Tôi vốn đã chạy kiểm tra sức khỏe tự động cho việc thu thập của mình, nên tôi bắt đầu công bố kết quả — một danh sách proxy miễn phí **thực sự được kiểm chứng**, kiểm tra lại mỗi 30 phút và tải được từ liên kết CDN ổn định. Không đăng ký, không thẻ tín dụng, không bảng điều khiển. Chỉ có vậy. Nếu nó giúp bạn tiết kiệm buổi chiều mà tôi đã mất, một ngôi sao sẽ giúp lập trình viên tiếp theo tìm thấy nó. Dữ liệu vẫn luôn miễn phí.

## 🚀 Sao chép và dùng

Mỗi định dạng một lệnh. Đường dẫn ổn định, không thay đổi.

```shell
# Tất cả proxy
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt -o proxies.txt

# SOCKS5
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt -o socks5.txt
```

## 📦 Tải tệp

| Danh sách | Proxy | TXT | JSON | CSV | CDN |
| --- | --- | --- | --- | --- | --- |
| **Tất cả proxy** | `4,196` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) |
| HTTP | `1,090` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/http.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) |
| HTTPS | `1,587` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/https.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) |
| SOCKS4 | `930` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks4.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) |
| SOCKS5 | `589` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) |
| Proxy nhanh | `790` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) |
| Proxy ổn định | `1,550` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/stability/stable/data.txt) |
| Proxy elite | `2,998` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/anonymity/elite/data.txt) |

**Duyệt theo quốc gia:** [Indonesia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/id/data.txt), [United States](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/us/data.txt), [China](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/cn/data.txt), [India](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/in/data.txt), [Bangladesh](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/bd/data.txt), [Philippines](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ph/data.txt), [Mexico](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/mx/data.txt), [Brazil](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/br/data.txt), [Colombia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/co/data.txt), [Vietnam](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/vn/data.txt), [Germany](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/de/data.txt), [Russia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ru/data.txt), [Thailand](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/th/data.txt), [Canada](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ca/data.txt), [Hong Kong](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/hk/data.txt), [Venezuela](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ve/data.txt), [France](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/fr/data.txt), [Japan](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/jp/data.txt), [Singapore](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/sg/data.txt), [Netherlands](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/nl/data.txt), [Ecuador](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ec/data.txt), [Italy](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/it/data.txt), [Cambodia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/kh/data.txt), [Spain](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/es/data.txt) — [Xem tất cả](https://github.com/xyzs996/free-proxy-health-list/tree/main/proxies/countries)

## 📊 Tỷ lệ hoạt động đo được

Hầu hết danh sách proxy đều tuyên bố đã kiểm chứng nhưng không nơi nào công bố con số. Dự án này công bố: lấy mẫu ngẫu nhiên từ danh sách đã phát hành, tải đầu-cuối qua từng proxy tới một URL bên thứ ba, và kết quả được phát hành cùng dữ liệu.

<img src="./assets/reliability-chart.png" width="640" alt="Tỷ lệ hoạt động đo được">

| Danh sách | Hoạt động trong mẫu |
| --- | --- |
| **Mẫu gần nhất** | **40%** (mẫu 400) |

<sub>Phương pháp: lấy mẫu ngẫu nhiên, tải đầu-cuối qua proxy, hết hạn 8 giây — `http://api.ipify.org/, http://icanhazip.com/, https://api.ipify.org/, https://icanhazip.com/`</sub>

## 🧭 Hướng dẫn theo tình huống

- **[Proxy cho web scraping](https://xyzs996.github.io/free-proxy-health-list/vi/use-cases/proxy-for-web-scraping.html)** — Xoay IP để tránh giới hạn tần suất và chặn.
- **[Proxy trong Python requests](https://xyzs996.github.io/free-proxy-health-list/vi/use-cases/python-requests-proxy.html)** — Ví dụ HTTP và SOCKS5 kèm thử lại.
- **[Xây pool proxy xoay vòng](https://xyzs996.github.io/free-proxy-health-list/vi/use-cases/rotating-proxy.html)** — Vòng lặp xoay hoạt động trong khoảng 20 dòng.
- **[Middleware proxy cho Scrapy](https://xyzs996.github.io/free-proxy-health-list/vi/use-cases/proxy-for-scrapy.html)** — Middleware cắm vào là chạy, tự xoay khi lỗi.
- **[Tùy chọn proxy của curl](https://xyzs996.github.io/free-proxy-health-list/vi/use-cases/proxy-for-curl.html)** — Cờ HTTP, HTTPS và SOCKS kèm lệnh thực tế.

## 🌐 Duyệt theo giao thức

- [HTTP](https://xyzs996.github.io/free-proxy-health-list/vi/protocols/http.html) — Đơn giản nhất cho yêu cầu web. Hoạt động với mọi client HTTP.
- [HTTPS](https://xyzs996.github.io/free-proxy-health-list/vi/protocols/https.html) — Proxy HTTP đã được kiểm chứng có thể tạo đường hầm TLS qua CONNECT.
- [SOCKS4](https://xyzs996.github.io/free-proxy-health-list/vi/protocols/socks4.html) — Đường hầm cũ, nhẹ, dành cho TCP thuần.
- [SOCKS5](https://xyzs996.github.io/free-proxy-health-list/vi/protocols/socks5.html) — Mọi lưu lượng TCP, kèm UDP và DNS từ xa.

## 🧱 Cấu trúc dữ liệu

`data.txt` mỗi dòng một `host:port`. `data.json` kèm siêu dữ liệu sức khỏe của từng mục:

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

Đọc bằng chương trình? [`llms.txt`](https://xyzs996.github.io/free-proxy-health-list/llms.txt) trả về toàn bộ ảnh chụp trong một yêu cầu — mỗi danh sách kèm số lượng, đường dẫn tải và ngày kiểm tra.

## 🔗 Dự án liên quan

Cùng một người duy trì, cùng một ý tưởng — dữ liệu công khai đọc được mà không cần tài khoản:

- **[Free LLM API list](https://github.com/xyzs996/free-llm-api)** — hạn mức miễn phí vĩnh viễn; mọi giới hạn công bố đều dẫn về nguồn chính thức.
- **[LLM API pricing list](https://github.com/xyzs996/llm-api-pricing/blob/main/README_VI.md)** — chi phí thực sự của các agent lập trình AI. Mọi con số trong các bài viết gom vào [một bảng](https://xyzs996.github.io/llm-api-pricing/figures.html), mỗi dòng kèm câu văn nó xuất phát ([JSON](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.json) / [CSV](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.csv)). Bắt đầu từ [hoá đơn token thực sự đi đâu](https://xyzs996.github.io/llm-api-pricing/topics/token-optimization.html).

## ❓ Câu hỏi thường gặp

<details>
<summary><strong>Những proxy miễn phí này có an toàn không?</strong></summary>

Proxy công khai miễn phí được dùng chung và do các bên không rõ danh tính vận hành, vì vậy đừng gửi mật khẩu, token hay dữ liệu cá nhân qua chúng. Hãy dùng để kiểm thử, thu thập trang công khai và tự động hóa — không dùng cho lưu lượng nhạy cảm.
</details>

<details>
<summary><strong>Danh sách được cập nhật bao lâu một lần?</strong></summary>

Mỗi proxy được kiểm tra lại và danh sách được phát hành lại sau mỗi 30 phút. Mỗi bản ghi JSON đều có lastChecked và độ trễ để bạn tự loại bỏ mục cũ hoặc chậm.
</details>

<details>
<summary><strong>'Đã kiểm chứng' ở đây nghĩa là gì?</strong></summary>

Mỗi mục đã hoàn tất bắt tay đúng giao thức và chuyển tiếp một yêu cầu thật theo kiểu đầu-cuối trước khi được phát hành. Những mục chỉ chấp nhận kết nối TCP sẽ không được phát hành.
</details>

<details>
<summary><strong>Vì sao một số proxy ngừng hoạt động chỉ sau vài phút?</strong></summary>

Proxy miễn phí vốn không ổn định — chúng liên tục xuất hiện rồi biến mất. Chính vì vậy danh sách được kiểm tra lại mỗi 30 phút và sắp xếp nhanh nhất trước. Hãy luôn chuyển sang mục kế tiếp khi gặp lỗi.
</details>

<details>
<summary><strong>Nên dùng loại proxy nào?</strong></summary>

HTTP đơn giản nhất cho yêu cầu web. SOCKS5 xử lý mọi lưu lượng TCP cùng UDP và DNS từ xa. SOCKS4 là lựa chọn cũ, nhẹ hơn. Các mục HTTPS là proxy HTTP đã được kiểm chứng có thể tạo đường hầm TLS.
</details>

<details>
<summary><strong>Tôi có cần đăng ký hoặc gắn sao cho kho lưu trữ không?</strong></summary>

Không. Danh sách là ảnh chụp hoàn toàn công khai trên các URL ổn định, không cần tài khoản và không cần thẻ tín dụng. Gắn sao chỉ giúp lập trình viên khác tìm thấy nó.
</details>

## 🧾 Những câu được trả lời đầy đủ, kèm số liệu

Các câu trả lời phía trên cố ý ngắn. Những câu này thì không: mỗi câu mở đầu bằng một câu trả lời trực tiếp, rồi đưa ra mọi con số đã đo được đằng sau nó, kèm cỡ mẫu và thời điểm đo:

- [How many free proxies actually work? Here is the measured rate, by protocol.](https://github.com/xyzs996/free-proxy-health-list/discussions/2) — the measured end-to-end success rate of a random sample, broken out by protocol, with the method and the timeout it was measured under.
- [Where do I get a free proxy list by country, and how many are in each?](https://github.com/xyzs996/free-proxy-health-list/discussions/3) — the per-country file path, how many entries each country has in the current snapshot, and how thin the tail gets.
- [How do I check whether a free proxy actually works?](https://github.com/xyzs996/free-proxy-health-list/discussions/4) — a working checker in ten lines, plus the four ways a naive check calls a dead proxy alive.

## ⚡ Cần độ tin cậy cho môi trường sản xuất?

Danh sách trên GitHub là ảnh chụp công khai miễn phí, không có SLA. Pro API bổ sung kiểm tra thường xuyên hơn, lọc theo giao thức, quốc gia và độ trễ, điểm cuối xoay vòng và giám sát mức dùng.

[Đăng ký truy cập sớm](https://xyzs996.github.io/free-proxy-health-list/vi/api.html)

## ⚖️ Giới hạn của ảnh chụp công khai

Proxy công khai miễn phí được dùng chung và vận hành bởi các bên không rõ danh tính. Đừng bao giờ gửi mật khẩu, token hay dữ liệu cá nhân qua chúng. Hãy tuân thủ Chính sách Sử dụng Chấp nhận được của GitHub: không spam, không tấn công, không vượt kiểm soát truy cập, không thu thập trái chính sách của trang.

## 🤝 Contributing

Hoan nghênh đóng góp cho tài liệu, ví dụ và tính dễ dùng của dữ liệu. Xem [CONTRIBUTING.md](./CONTRIBUTING.md)

Không cần nguồn, không cần ảnh chụp màn hình, không cần pull request — [bạn cần proxy ở nước nào, và danh sách này có không?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_VI.md)

## 📄 License

[MIT](./LICENSE)
