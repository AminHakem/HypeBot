from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def setup(launching, profile):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2F"
               "www.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    driver.find_element_by_name("identifier").send_keys("Gogetaatss12@gmail.com"+Keys.RETURN)
    time.sleep(1)
    if launching:
        driver.find_element_by_name("password").send_keys(profile["password"]+Keys.RETURN)
    return driver

# setup() method initiates web driver, sets headless or not, and logs into google chrome
# sleep_time is the amount of seconds user wants to type in their google password


def add_to_cart(driver, item):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "inner-article")))
    driver.find_elements_by_class_name("inner-article")[item].click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.NAME, "commit")))
    driver.find_element_by_name("commit").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'checkout')]")))
    time.sleep(1)
    driver.get("https://www.supremenewyork.com/checkout")
# add_to_cart() selects item from list of "inner-article" objects then loads checkout page


def checkout(driver, profile):
    checkout_fields = driver.find_elements_by_tag_name("input")
#   print (len(checkout_fields))
    billing_info(driver, profile)
    card_info(driver, checkout_fields, profile)


def billing_info(driver, profile):
    name = driver.find_element_by_id("order_billing_name")
    name.send_keys(profile["name"])
    time.sleep(1000000)
    # checkout_fields[2].send_keys(profile["name"])
    # checkout_fields[3].send_keys(profile["email"])
    # checkout_fields[4].send_keys(profile["phone"])  # of phone string doesn't enter which is why we send 5 first
    # checkout_fields[5].send_keys(profile["address"])
    # checkout_fields[7].send_keys(profile["zipcode"])
    # checkout_fields[8].send_keys(profile["city"])


# billing_info() fills out checkout page up to zipcode


def card_info(driver, checkout_fields, profile):
    card = checkout_fields[13]
    num = profile["card#"]
    card.send_keys(num[0:1])
    card.send_keys(num[1:2])
    card.send_keys(num[2:3])
    card.send_keys(num[3:4])
    card.send_keys(num[4:5])
    card.send_keys(num[5:6])
    card.send_keys(num[6:7])
    card.send_keys(num[7:8])
    card.send_keys(num[8:9])
    card.send_keys(num[9:10])
    card.send_keys(num[10:11])
    card.send_keys(num[11:12])
    card.send_keys(num[12:13])
    card.send_keys(num[13:14])
    card.send_keys(num[14:15])
    card.send_keys(num[15:])
    driver.find_elements_by_tag_name('ins')[1].click()
    driver.find_element_by_id("credit_card_month").click()  # THESE ARE NOT REGULAR STRINGS FOR YEAR AND MONTH
    driver.find_element_by_xpath(profile["month"]).click()
    driver.find_element_by_id("credit_card_year").click()  # THESE ARE NOT REGULAR STRINGS FOR YEAR AND MONTH
    driver.find_element_by_xpath(profile["year"]).click()  # This string being passed is an xpath. Needs fixing
    #  checkout_fields[14].send_keys(profile["cvv"]) #  + Keys.RETURN)
# card_info fills out card information and then sends Keys.RETURN to submit the order
