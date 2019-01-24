import requests


def getPageInfo(url,headers,page):
    try:
        res = requests.get(url,headers=headers,timeout=20)
        if res.status_code == 200:
            return res.text
    except Exception as e:
        print(e)

def main():
    url = "https://maoyan.com/board/4";

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    page = 10;
    a = getPageInfo(url,headers,page)
    print(a)

if __name__ == '__main__':
    main()