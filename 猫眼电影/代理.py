from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

url = 'https://www.python.org/'

proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:9734',
    'https': 'https://127.0.0.1:9734',
})

opener = build_opener(proxy_handler)

try:
    response = opener.open(url)
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
