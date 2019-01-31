from selenium import webdriver
bowser = webdriver.Chrome()

try:
    bowser.get('http://www.luofq.com')
    input_first = bowser.find_element_by_css_selector('#s')
    print(input_first)
except Exception as e:
    print(e)