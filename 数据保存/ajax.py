import requests

keyword = "街拍"
url = "https://www.toutiao.com/api/search/content/?aid=24&offset=0&format=json&keyword=%s"%(keyword)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

data = {
    "aid":24,
    "offset":0,
    "format":"json",
    "keyword":"街拍",
    "autoload":"true",
    "count":20,
    "cur_tab":1,
    "from":"search_tab",
    "pd":"synthesis"
}

res = requests.get(url=url,headers=headers,data=data)
res = res.json()
data = res['data']

for i in data:
    try:
        print(i['title'])
    except:
        pass