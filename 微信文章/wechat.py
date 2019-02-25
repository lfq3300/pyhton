from selenium import  webdriver
bowser = webdriver.Chrome()
try:
    bowser.get("https://weixin.sogou.com/")
    query = bowser.find_element_by_id("query")
    query.send_keys("人工智能")
    button = bowser.find_element_by_css_selector(".swz")
    button.click()

except Exception as e:
    print(e)