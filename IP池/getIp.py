#爬取IP池
from selenium import webdriver
import re

bowser = webdriver.Chrome()

def OpenXiCiDaiLiPage():
    page = 1;
    url = "https://www.xicidaili.com/nn/%s" % (page)
    bowser.get(url)
    ipList = bowser.find_elements_by_xpath("//tr")
    for i in ipList:
        dailiInfo = i.text.split(" ");
        compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if compile_ip.match(dailiInfo[0]):
            host = "%s:%s" % (dailiInfo[0],dailiInfo[1])
            print(host)

if __name__ == '__main__':
    OpenXiCiDaiLiPage()