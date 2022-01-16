#引入selenium裡的webdriver類別
from selenium import webdriver

from common import *
#初始化Chrome瀏覽器的driver

browser = webdriver.Chrome("chromedriver")
    
login_IG(browser, "NewmanLai2022", "1qaz!QAZ")
