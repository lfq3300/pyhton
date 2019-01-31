from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.luofq.com")
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("完成")')