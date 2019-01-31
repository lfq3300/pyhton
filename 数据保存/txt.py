import requests
from pyquery import PyQuery as pq
url = "https://www.zhihu.com/explore"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
doc = pq(url=url,headers=headers)
#获取知乎标题
items = doc('.question_link').items()
file = open("知乎标题--信息.txt",'w',encoding='utf-8');
for i in items:
    str = "标题：%s    ----- 链接：%s \n" % (i.text(),i.attr('href'))
    file.write(str)
file.close();