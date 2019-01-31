from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

borwser = webdriver.Chrome()

try:
    borwser.get("https://www.baidu.com/")
    input = borwser.find_element_by_id('kw')
    input.send_keys('数据库')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(borwser,10)
    wait.until(EC.presence_of_all_elements_located((By.ID,'content_left')))
    print(borwser.current_url)
    print(borwser.get_cookies())
  #  print(borwser.page_source)
finally:
    borwser.close()