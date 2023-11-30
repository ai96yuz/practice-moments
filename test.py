# import time
# from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
#
# from constants import *
# from solver import *
#
# # driver = webdriver.Firefox()
#
# driver = webdriver.Chrome()
# driver.get("https://visa.vfsglobal.com/blr/ru/pol/login")
# time.sleep(10)
# elem = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
# elem.send_keys(username)
# time.sleep(5)
# elem = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
# elem.send_keys(password)
# time.sleep(4)
#
# checkbox = driver.find_element(By.XPATH, '//*[@id="challenge-stage"]')
#
# # C4PTCH4 solver ///
#
# # if not checkbox.is_selected():
# #     checkbox.click()
# #
# # time.sleep(15)
# # checkbox.click()
# #
# # time.sleep(15)
# # checkbox.click()
#
# # submit_button = driver.find_element(By.ID, "submit")
# # submit_button.click()
#
# time.sleep(60)
#
# driver.close()


import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
PROXY = "212.237.16.60:3128"
#
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     "noProxy": None,
#     "proxyType": "MANUAL",
#     "class": "org.openqa.selenium.Proxy",
#     "autodetect": False
# }
chrome_options.add_argument(f'--proxy-server={PROXY}')

# you have to use remote, otherwise you'll have to code it yourself in python to


driver = webdriver.Chrome()
driver.get("https://visa.vfsglobal.com/tur/en/pol/login")
time.sleep(10)
print(driver.title)
# email = driver.find_element(by=By.ID, value='mat-input-0')
email = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
password = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
# password = driver.find_element(by=By.ID, value='mat-input-1')
email.send_keys("dd810a5ed8@catdogmail.live")
password.send_keys("Dd810a5ed8@")
# email.send_keys(Keys.RETURN)
time.sleep(5)
# Start new Booking
driver.find_element(By.XPATH, "/html/body/app-root/div/app-dashboard/section/div/div[2]/button").click()
###################
driver.find_element(By.ID, "mat-select-0").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div/mat-option[3]/span").click()
