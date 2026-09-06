<!-- proxyhealthlist:generated — rebuilt by `proxyhealthlist build-site` from the published
     snapshot. Hand edits are overwritten on the next run; change the
     generator (proxyhealthlist/site/) or open an issue instead. -->
<div align="center">

<a href="https://xyzs996.github.io/free-proxy-health-list/tr/"><img src="./assets/og-image.png" alt="Ücretsiz proxy listesi — doğrulanmış HTTP, HTTPS, SOCKS4 ve SOCKS5" width="100%"></a>

# Free Proxy Health List

**Gerçekten doğrulanmış ücretsiz proxy listesi.**

[![total](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Ftotal.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/total.json) [![http](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fhttp.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/http.json) [![socks5](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fsocks5.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/socks5.json) [![updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Fupdated.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/updated.json) [![reliability](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fxyzs996%2Ffree-proxy-health-list@main%2Fproxies%2Fbadges%2Freliability.json&style=for-the-badge)](https://github.com/xyzs996/free-proxy-health-list/blob/main/proxies/badges/reliability.json)
[![Validate snapshot](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml/badge.svg)](https://github.com/xyzs996/free-proxy-health-list/actions/workflows/validate-snapshot.yml)
[![Stars](https://img.shields.io/github/stars/xyzs996/free-proxy-health-list?style=for-the-badge&logo=github)](https://github.com/xyzs996/free-proxy-health-list/stargazers)

[🌐 İndir](https://xyzs996.github.io/free-proxy-health-list/tr/) · [⚡ Pro API](https://xyzs996.github.io/free-proxy-health-list/tr/api.html) · [📊 Bir yapay zeka ajanını çalıştırmak kaça geliyor?](https://github.com/xyzs996/llm-api-pricing) · [💬 Hangi ülke lazım?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_TR.md) · [🐞 Issues](https://github.com/xyzs996/free-proxy-health-list/issues)

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md) · [Русский](./README_RU.md) · **Türkçe** · [Bahasa Indonesia](./README_ID.md) · [Tiếng Việt](./README_VI.md)

</div>

> Genel anlık görüntü · her 30 dakikada güncellenir · kayıt gerekmez

## 💡 Bu proje neden var?

Bir süre önce küçük bir fiyat takip kazıyıcısı yazıyordum. Tek IP'den yapılan her çalıştırma hız sınırına takılıyordu, ben de ücretsiz proxy aramaya başladım. Bütün listeler aynı hikâyeyi anlatıyordu: girdilerin yarısı ölüydü, "günlük güncellenir" yazanlar aylardır yerinde duruyordu ve çalışan proxy'si olan siteler daha denemeden kredi kartı istiyordu.

Kendi kazıma işim için zaten otomatik sağlık kontrolleri çalıştırıyordum, bu yüzden sonuçları yayımlamaya başladım — **gerçekten doğrulanmış**, her 30 dakikada bir yeniden kontrol edilen ve kararlı bir CDN bağlantısından çekilebilen ücretsiz bir proxy listesi. Kayıt yok, kart yok, panel yok. Hepsi bu. Benim kaybettiğim öğleden sonrayı size kazandırırsa, bir yıldız sonraki geliştiricinin bulmasına yardım eder. Veri her hâlükârda ücretsiz.

## 🚀 Kopyala ve kullan

Her biçim için tek komut. Değişmeyen kararlı yollar.

```shell
# Tüm proxy'ler
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt -o proxies.txt

# SOCKS5
curl -sL https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt -o socks5.txt
```

## 📦 Dosyaları indir

| Liste | Proxy | TXT | JSON | CSV | CDN |
| --- | --- | --- | --- | --- | --- |
| **Tüm proxy'ler** | `4,196` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/all.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/all/data.txt) |
| HTTP | `1,090` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/http.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/http/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/http/data.txt) |
| HTTPS | `1,587` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/https.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/https/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/https/data.txt) |
| SOCKS4 | `930` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks4.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks4/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks4/data.txt) |
| SOCKS5 | `589` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/socks5.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/protocols/socks5/data.txt) |
| Hızlı proxy'ler | `790` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/latency/fast/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/latency/fast/data.txt) |
| Kararlı proxy'ler | `1,550` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/stability/stable/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/stability/stable/data.txt) |
| Elit proxy'ler | `2,998` | [TXT](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.txt) | [JSON](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.json) | [CSV](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/anonymity/elite/data.csv) | [jsDelivr](https://cdn.jsdelivr.net/gh/xyzs996/free-proxy-health-list@main/proxies/anonymity/elite/data.txt) |

**Ülkeye göre:** [Indonesia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/id/data.txt), [United States](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/us/data.txt), [China](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/cn/data.txt), [India](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/in/data.txt), [Bangladesh](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/bd/data.txt), [Philippines](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ph/data.txt), [Mexico](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/mx/data.txt), [Brazil](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/br/data.txt), [Colombia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/co/data.txt), [Vietnam](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/vn/data.txt), [Germany](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/de/data.txt), [Russia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ru/data.txt), [Thailand](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/th/data.txt), [Canada](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ca/data.txt), [Hong Kong](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/hk/data.txt), [Venezuela](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ve/data.txt), [France](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/fr/data.txt), [Japan](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/jp/data.txt), [Singapore](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/sg/data.txt), [Netherlands](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/nl/data.txt), [Ecuador](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/ec/data.txt), [Italy](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/it/data.txt), [Cambodia](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/kh/data.txt), [Spain](https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/countries/es/data.txt) — [Tümünü gör](https://github.com/xyzs996/free-proxy-health-list/tree/main/proxies/countries)

## 📊 Ölçülen çalışma oranı

Neredeyse her proxy listesi doğrulandığını iddia eder ama hiçbiri sayı yayımlamaz. Bu proje yayımlıyor: yayımlanan listeden rastgele bir örneklem alınıp her proxy üzerinden üçüncü taraf bir URL uçtan uca çekiliyor ve sonuç veriyle birlikte yayımlanıyor.

<img src="./assets/reliability-chart.png" width="640" alt="Ölçülen çalışma oranı">

| Liste | Örneklemde çalışan |
| --- | --- |
| **Son örneklem** | **40%** (400 örneklendi) |

<sub>Yöntem: rastgele örneklem, proxy üzerinden uçtan uca istek, 8 sn zaman aşımı — `http://api.ipify.org/, http://icanhazip.com/, https://api.ipify.org/, https://icanhazip.com/`</sub>

## 🧭 Kullanım senaryosu rehberleri

- **[Web kazıma için proxy](https://xyzs996.github.io/free-proxy-health-list/tr/use-cases/proxy-for-web-scraping.html)** — Limit ve engelleri aşmak için IP değiştirin.
- **[Python requests proxy](https://xyzs996.github.io/free-proxy-health-list/tr/use-cases/python-requests-proxy.html)** — Yeniden denemeli HTTP ve SOCKS5 örnekleri.
- **[Dönen proxy havuzu kurun](https://xyzs996.github.io/free-proxy-health-list/tr/use-cases/rotating-proxy.html)** — Yaklaşık 20 satırda çalışan döngü.
- **[Scrapy proxy ara katmanı](https://xyzs996.github.io/free-proxy-health-list/tr/use-cases/proxy-for-scrapy.html)** — Hatada değiştiren hazır ara katman.
- **[curl proxy seçenekleri](https://xyzs996.github.io/free-proxy-health-list/tr/use-cases/proxy-for-curl.html)** — Gerçek komutlarla HTTP, HTTPS ve SOCKS.

## 🌐 Protokole göre

- [HTTP](https://xyzs996.github.io/free-proxy-health-list/tr/protocols/http.html) — Web istekleri için en basiti. Her HTTP istemcisiyle çalışır.
- [HTTPS](https://xyzs996.github.io/free-proxy-health-list/tr/protocols/https.html) — CONNECT ile TLS tünellediği doğrulanmış HTTP proxy'leri.
- [SOCKS4](https://xyzs996.github.io/free-proxy-health-list/tr/protocols/socks4.html) — Ham TCP için hafif, eski tünel.
- [SOCKS5](https://xyzs996.github.io/free-proxy-health-list/tr/protocols/socks5.html) — Her türlü TCP trafiği, ayrıca UDP ve uzak DNS.

## 🧱 Veri yapısı

`data.txt` her satırda bir `host:port` içerir. `data.json` her girdinin sağlık meta verisini taşır:

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

Bunu bir programla mı okuyorsunuz? [`llms.txt`](https://xyzs996.github.io/free-proxy-health-list/llms.txt) tüm anlık görüntüyü tek istekte verir — her listenin sayısı, indirme adresleri ve kontrol tarihi.

## 🔗 İlgili projeler

Aynı bakımcı, aynı fikir — hesap açmadan okuyabileceğiniz açık veri:

- **[Free LLM API list](https://github.com/xyzs996/free-llm-api)** — kalıcı ücretsiz kotalar; yayımlanan her sınır resmî kaynağına bağlı.
- **[LLM API pricing list](https://github.com/xyzs996/llm-api-pricing)** — yapay zekâ kodlama ajanlarının gerçek maliyeti. Yazılardaki her sayı [tek bir tabloda](https://xyzs996.github.io/llm-api-pricing/figures.html), her satır alındığı cümleyle birlikte ([JSON](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.json) / [CSV](https://cdn.jsdelivr.net/gh/xyzs996/llm-api-pricing@main/data/figures.csv)). [Token faturası gerçekte nereye gidiyor](https://xyzs996.github.io/llm-api-pricing/topics/token-optimization.html) ile başlayın.

## ❓ Sıkça sorulan sorular

<details>
<summary><strong>Bu ücretsiz proxy'ler güvenli mi?</strong></summary>

Ücretsiz genel proxy'ler paylaşımlıdır ve kimliği bilinmeyen kişilerce işletilir; bu yüzden asla parola, token veya kişisel veri göndermeyin. Test, genel sayfaların kazınması ve otomasyon için uygundur; hassas trafik için değil.
</details>

<details>
<summary><strong>Liste ne sıklıkla güncelleniyor?</strong></summary>

Her proxy yeniden kontrol edilir ve liste her 30 dakikada bir yeniden yayımlanır. Her JSON kaydında lastChecked ve gecikme değeri bulunur; eski veya yavaş girdileri kendiniz eleyebilirsiniz.
</details>

<details>
<summary><strong>Buradaki 'doğrulanmış' tam olarak ne demek?</strong></summary>

Her girdi, yayımlanmadan önce protokole uygun bir el sıkışmayı tamamladı ve gerçek bir isteği uçtan uca iletti. Yalnızca TCP bağlantısına yanıt veren girdiler yayımlanmaz.
</details>

<details>
<summary><strong>Neden bazı proxy'ler dakikalar içinde çalışmaz oluyor?</strong></summary>

Ücretsiz proxy'ler doğası gereği değişkendir; sürekli ortaya çıkar ve kaybolur. Liste tam da bu yüzden her 30 dakikada yeniden kontrol edilir ve en hızlıdan sıralanır. Hata durumunda daima bir sonraki girdiye geçin.
</details>

<details>
<summary><strong>Hangi proxy türünü kullanmalıyım?</strong></summary>

Web istekleri için en basiti HTTP'dir. SOCKS5 her türlü TCP trafiğinin yanı sıra UDP ve uzak DNS'i destekler. SOCKS4 daha hafif, eski bir seçenektir. HTTPS girdileri, TLS tünellediği doğrulanmış HTTP proxy'leridir.
</details>

<details>
<summary><strong>Kayıt olmam veya depoya yıldız vermem gerekir mi?</strong></summary>

Hayır. Liste, kararlı URL'lerde tamamen genel bir anlık görüntüdür; hesap da kredi kartı da gerekmez. Yıldız yalnızca diğer geliştiricilerin bulmasına yardımcı olur.
</details>

## 🧾 Sayılarıyla birlikte uzun uzun yanıtlananlar

Yukarıdaki yanıtlar bilerek kısa. Bunlar değil: her biri önce doğrudan bir yanıt veriyor, ardından o yanıtın arkasındaki ölçülmüş her sayıyı örneklem büyüklüğü ve ölçüm zamanıyla birlikte gösteriyor:

- [How many free proxies actually work? Here is the measured rate, by protocol.](https://github.com/xyzs996/free-proxy-health-list/discussions/2) — the measured end-to-end success rate of a random sample, broken out by protocol, with the method and the timeout it was measured under.
- [Where do I get a free proxy list by country, and how many are in each?](https://github.com/xyzs996/free-proxy-health-list/discussions/3) — the per-country file path, how many entries each country has in the current snapshot, and how thin the tail gets.
- [How do I check whether a free proxy actually works?](https://github.com/xyzs996/free-proxy-health-list/discussions/4) — a working checker in ten lines, plus the four ways a naive check calls a dead proxy alive.

## ⚡ Üretim güvenilirliği mi gerekiyor?

GitHub listesi, SLA'sız ücretsiz bir genel anlık görüntüdür. Pro API daha sık kontroller, protokol, ülke ve gecikmeye göre filtreleme, dönen uç nokta ve kullanım izleme sunar.

[Erken erişime katıl](https://xyzs996.github.io/free-proxy-health-list/tr/api.html)

## ⚖️ Genel anlık görüntü sınırları

Ücretsiz genel proxy'ler paylaşımlıdır ve kimliği bilinmeyen taraflarca işletilir. Asla parola, token veya kişisel veri göndermeyin. GitHub Kabul Edilebilir Kullanım Politikalarına uyun: spam yok, saldırı yok, erişim denetimlerini aşma yok, site politikalarına aykırı kazıma yok.

## 🤝 Contributing

Belgeler, örnekler ve veri kullanılabilirliği için katkılar memnuniyetle karşılanır. Bkz. [CONTRIBUTING.md](./CONTRIBUTING.md)

Kaynak, ekran görüntüsü ya da pull request gerekmez — [hangi ülke lazımdı ve bu listede var mıydı?](https://github.com/xyzs996/free-proxy-health-list/issues/new?template=country.yml&came_from=README_TR.md)

## 📄 License

[MIT](./LICENSE)
