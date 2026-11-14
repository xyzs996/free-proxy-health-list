from playwright.sync_api import sync_playwright


PROXY = "http://127.0.0.1:8080"


with sync_playwright() as p:
    browser = p.chromium.launch(proxy={"server": PROXY})
    page = browser.new_page()
    page.goto("http://example.com/", wait_until="domcontentloaded")
    print(page.title())
    browser.close()
