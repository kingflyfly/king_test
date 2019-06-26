from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://192.168.9.1/html/reboot.html")
    browser.find_element_by_id("logout_span").click()
    browser.find_element_by_id('username').send_keys("admin")
    browser.find_element_by_id('password').send_keys("Wy@2013!")
    browser.find_element_by_id("pop_login").click()
    time.sleep(1)
    browser.find_element_by_id("settings").click()
    browser.find_element_by_id("label_system").click()
    time.sleep(1)
    browser.find_element_by_id("label_reboot").click()
    browser.find_element_by_id("undefined").click()
    time.sleep(1)
    browser.find_element_by_id("pop_confirm").click()
except:
    print(1)