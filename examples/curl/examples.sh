#!/usr/bin/env sh
set -eu

# Download all proxies as host:port lines.
curl -sL "https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/all/data.txt" \
  -o proxies.txt

# Download SOCKS5 proxies only.
curl -sL "https://raw.githubusercontent.com/xyzs996/free-proxy-health-list/main/proxies/protocols/socks5/data.txt" \
  -o socks5.txt

# Test one HTTP proxy manually.
proxy="$(head -n 1 proxies.txt)"
curl -x "http://$proxy" -I "http://example.com/" --max-time 10
