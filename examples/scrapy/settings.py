# Minimal Scrapy proxy example. Replace PROXY with a value from proxies/all/data.txt.

PROXY = "http://127.0.0.1:8080"

DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 110,
}

DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "proxyhealthlist-example/0.1",
}


def apply_proxy(request):
    request.meta["proxy"] = PROXY
