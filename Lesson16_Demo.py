#引入selenium裡的webdriver類別
from selenium import webdriver
from selenium.webdriver.common.by import By
#初始化Chrome瀏覽器的driver
browser = webdriver.Chrome("chromedriver")
#使用browser發出get請求
browser.get("https://www.google.com")

search_input_xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input"

#找尋Chrome的搜尋的輸入方塊
search_element = browser.find_element_by_xpath(search_input_xpath)
search_element.send_keys("海賊王")

body = browser.find_element_by_tag_name("body")
body.click()

search_submit_xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]"
search_submit_btn = browser.find_element(By.XPATH, search_submit_xpath)
search_submit_btn.click()
