import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

from constants import *
from solver import *

# driver = webdriver.Firefox()

driver = webdriver.Chrome()
driver.get("https://visa.vfsglobal.com/blr/ru/pol/login")
time.sleep(10)
elem = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
elem.send_keys(username)
time.sleep(5)
elem = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
elem.send_keys(password)
time.sleep(4)

checkbox = driver.find_element(By.XPATH, '//*[@id="challenge-stage"]')

# C4PTCH4 solver ///

# if not checkbox.is_selected():
#     checkbox.click()
#
# time.sleep(15)
# checkbox.click()
#
# time.sleep(15)
# checkbox.click()

# submit_button = driver.find_element(By.ID, "submit")
# submit_button.click()

time.sleep(60)

driver.close()
