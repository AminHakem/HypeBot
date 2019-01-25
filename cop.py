import time
import threading
import BotMethods
import profile

Person = profile.Amin
driver = BotMethods.setup(True, Person)
# setup() method takes boolean value launching.
# If set to true driver will go headless and will log into google

driver.get("http://www.supremenewyork.com/shop/new")

# print("loaded")

numSoldOut = len(driver.find_elements_by_xpath("//*[contains(text(), 'sold out')]"))

# Loop to refresh page until drop. Refreshes every 2 seconds and exits when there are 5 items less sold out
while False:
    driver.get("http://www.supremenewyork.com/shop/new")
    articlesSoldOut = driver.find_elements_by_xpath("//*[contains(text(), 'sold out')]")
    if len(articlesSoldOut) < numSoldOut-5:
            break
    time.sleep(1)
    numSoldOut = len(articlesSoldOut)

start_time = time.time()

BotMethods.add_to_cart(driver, 46)
BotMethods.checkout(driver, Person)

print("Copped in " + str(time.time() - start_time)+" seconds!")
