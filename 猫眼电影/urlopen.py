import urllib.request

url = 'https://www.python.org/'

'''
data 请求url所访问的参数 使用data后 请求方式改为post  不再是get
data = bytes(url.parse.)
urlopen(url,data,timeout)

'''

response = urllib.request.urlopen(url)
# 获取网页状态码
print(response.status)
#获取请求头信息
print(response.getheaders())
#获取服务器
print(response.getheader('Server'))
# 打印网页内容
#print(response.read().decode('utf-8'))

