import urllib.request
import urllib.parse
url = 'https://www.python.org/'

'''
Request 函数

Request(url, data=None, headers={},origin_req_host=None, unverifiable=False,method=None)

url 请求访问地址

data 参数 必须以字节流形式访问, 如果是字典类型 

data = {
    'name':'Luo'
}

bytes(urllib.parse.urlencode(data),encoding('UTF-8'))

header 请求头 伪装浏览器

origin_req_host 请求到IP地址

unverifiable 未知！

method 请求方式 get post ！

'''
request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))