'''
目标 抓取京东关键字为ipad的商品
抓取 图片 ,付款人数,价格 ,位置, 店铺名称
'''

from selenium import webdriver
import time
import os
import urllib.request
bowser = webdriver.Chrome()


def get_page_inof():
    pass

def write_to_file():
    pass


try:
    # 模仿浏览器打开
    bowser.get('https://search.jd.com/Search?keyword=ipad')

    # 找到下一页接口
    input_first = bowser.find_element_by_css_selector('.pn-next')
    # 获取当前页数  防止发生意外 需要记录当时页数
    page = bowser.find_element_by_css_selector('#J_bottomPage .p-num .curr').text

    goodslist = bowser.find_elements_by_css_selector("#J_goodsList .gl-item")
    fle = "京东商城Ipad信息"
    if not os.path.exists(fle):
        os.makedirs(fle)

    pagefle = fle+"/第"+page+"页商品信息"
    if not os.path.exists(pagefle):
        os.makedirs(pagefle)
    for goods in goodslist:
        #打印这页产品名称 / ID
        id = goods.get_attribute("data-sku")
        namefle = pagefle+"/"+id;
        if not os.path.exists(namefle):
            os.makedirs(namefle)
        file = open(namefle+"/商品信息.txt", 'w', encoding='utf-8')
        name = goods.find_element_by_css_selector(".p-name  a  em").text
        file.write("商品名称：%s" % (name))
        price = goods.find_element_by_css_selector(".p-price strong  i").text
        file.write("价格：%s" % (name))
        file.close()
        # img =  goods.find_element_by_css_selector(".p-img img").get_attribute("src")
        # file = open(namefle+"/id.png", 'wb')
        # file.write((urllib.request.urlopen(img).read()))
        # file.close()
    #time.sleep(5)
    # 点击下一页
   # input_first.click()
except Exception as e:
    print(e)