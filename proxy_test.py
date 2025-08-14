import sys
import requests
from urllib.parse import urlparse

if len(sys.argv) != 2:
    print(
        'proxy_test v1.0.1\n'
        'Simple utility to test proxy connections\n'
        'Supports HTTP and SOCKS5 proxies.\n\n'
        'Usage:\n'
        '  proxy_test protocol://[user:password@]address:port\n'
        '  (user and password are optional)\n\n'
        'Examples:\n'
        '  HTTP:   proxy_test http://john_doe:password@102.177.176.242:80\n'
        '  SOCKS5: proxy_test socks5://38.127.179.125:46656'
    )
    sys.exit(1)

proxy_url = sys.argv[1]

parsed = urlparse(proxy_url)

address = parsed.hostname
port = parsed.port

proxies = {
    'http': proxy_url,
    'https': proxy_url
}

test_url = 'http://httpbin.org/ip'
try:
    response = requests.get(test_url, proxies=proxies, timeout=10)
    response_json = response.json()
    public_ip = response_json.get('origin')
    print(f' {address}:{port}\tПрокси работает. IP: {public_ip}')

except requests.exceptions.RequestException as e:
    print(f' {address}:{port}\tОшибка прокси.')

except ValueError:
    pass
