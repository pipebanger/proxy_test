import sys
import requests
from urllib.parse import urlparse

if len(sys.argv) != 2:
    print('Использование: proxy_test.exe protocol://user:pass@address:port')
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
