import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def torchrome():
    PROXY = "socks5://127.0.0.1:9050"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    browser = webdriver.Chrome(executable_path="./drivers/chromedriver",options=chrome_options)

def login():
    browser.get("https://[site]"/)
    browser.find_element_by_name('email').send_keys('[email-to-login]')
    browser.find_element_by_name('password').send_keys('[password]')
    browser.find_element_by_xpath('//input[@value="submit"]').send_keys(Keys.ENTER)
    
 if __name__ == "__main__":
    torchrome()
    login()
