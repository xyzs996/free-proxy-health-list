# Contributing

Thanks for helping improve ProxyHealthList.

## Ways to Contribute

- Report dead sources or broken output files.
- Add examples for developer tools.
- Improve documentation and translations.
- Suggest safer quality signals.
- Report compliance concerns about a proxy source.

## Pull Requests

1. Keep PRs focused.
2. Do not add sources with unclear redistribution terms.
3. Do not add code that bypasses access controls or targets a specific third-party service for evasion.
4. Run the local publisher with a small limit before submitting:

```shell
python -m proxyhealthlist update --limit 50 --workers 20 --timeout 3
```

## Source Policy

Proxy sources must be public, must not require authentication, and must be removed if the owner asks to opt out.
