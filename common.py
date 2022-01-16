from selenium.webdriver.common.by import By
def login_IG(browser, username, password):
    browser.get("https://www.instagram.com/")
    browser.implicitly_wait(10) 
    
    username_input = browser.find_element(by=By.NAME, value="username")
    username_input.send_keys(username)
    password_input = browser.find_element(by=By.NAME, value="password")
    password_input.send_keys(password)
    
    login_btn_xpath = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button"
    login_btn = browser.find_element(by=By.XPATH, value=login_btn_xpath)
    login_btn.click()
    browser.implicitly_wait(10) 
