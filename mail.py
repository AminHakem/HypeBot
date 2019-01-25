from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2F"
               "www.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
time.sleep(1)
driver.find_element_by_id('identifierId').send_keys()
time.sleep(1)
driver.find_element_by_name("password").send_keys("ayyeitssaul7")
