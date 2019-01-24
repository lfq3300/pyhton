from urllib import request
import re

'''
 抓取不成功 
'''
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
    "Host":"www.zhihu.com",
}

url = "https://www.zhihu.com/explore";
res = request.Request(url=url,headers=headers)
r = request.urlopen(res)
print(r.read().decode('utf-8'))