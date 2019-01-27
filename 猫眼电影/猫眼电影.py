import requests
import re
import os
import urllib.request

#解析字符串获取标题等信息
def parse_one_page(url,headers,page):
    try:
        res = requests.get(url, headers=headers, timeout=20)
        if res.status_code == 200:
            html = res.text
            pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
        + '<a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?releasetime">(.*?)</p>'
        + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
            items = re.findall(pattern, html)
            for item in items:
                # yield
                yield {
                    'index':item[0],
                    'title': item[2],
                    'iamges': item[1],
                    'actor': item[3].strip(),
                    'time':item[4],
                    'score':item[5]+item[6]
                }
        else:
            pass;
    except Exception as e:
        print(e)

def main(page):
    url = "https://maoyan.com/board/4?offset=%s" % page
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    for item  in parse_one_page(url,headers,page):
        write_to_file(item)



#创建文件夹 保存电影信息
def write_to_file(content):
    try:
        index = content['index']
        actor = content['actor']
        title = content['title']
        time = content['time']
        score = content['score']
        iamges = content['iamges']

        root = "猫眼电影/" +index +"----"+ title
        if not os.path.exists(root):
            os.makedirs(root)
        else:
            txt = root + "/" + title + "--电影信息.txt"
            # 写入文件 下载图片
            file = open(txt, 'w', encoding='utf-8')
            str = "电影名称： " + title + "\n排名：" + index + "\n上映时间：" + time + "\n" + actor + "\n评分：" + score
            file.write(str)
            file.close()
            # 下载图片 二进制流的形式
            img = root + "/" + title + "--封面图.jpg"
            file = open(img, 'wb')
            file.write((urllib.request.urlopen(iamges).read()))
            file.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    if not os.path.exists('猫眼电影'):
        os.makedirs('猫眼电影')
    for i in range(10):
       main(i*10)
