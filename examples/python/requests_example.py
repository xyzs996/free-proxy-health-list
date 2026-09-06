import requests


PROXY_LIST_URL = (
    "https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/"
    "proxies/protocols/http/data.txt"
)


def main() -> None:
    proxies = requests.get(PROXY_LIST_URL, timeout=10).text.splitlines()
    proxy = proxies[0]
    response = requests.get(
        "http://example.com/",
        proxies={
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        },
        timeout=10,
    )
    print(proxy, response.status_code)


if __name__ == "__main__":
    main()
