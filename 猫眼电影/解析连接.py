from urllib.parse import urlparse

url = "http://www.luofq.com/index.html?id=15#home"
result = urlparse(url)
print(type(result),result)

