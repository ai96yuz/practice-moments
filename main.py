# import asyncio
#
# database = {
#     1: {"name": "John Doe", "email": "john@example.com"},
#     2: {"name": "Jane Smith", "email": "jane@example.com"},
# }
#
#
# async def search_users_in_db(query):
#     await asyncio.sleep(1)
#     results = []
#     for user_id, user_info in database.items():
#         if query.lower() in user_info["name"].lower():
#             results.append(user_info)
#     return results
#
#
# async def handle_form_input():
#     while True:
#         user_input = input('Enter data : ')
#         search_result = await search_users_in_db(user_input)
#         if not search_result:
#             print(f"No user with name '{user_input}' found. Please try again.")
#         else:
#             print(f"Search request complete: '{user_input}': {search_result}")
#
# try:
#     asyncio.run(handle_form_input())
# except KeyboardInterrupt:
#     print("\nExiting the program.")

import random
import time

import pyautogui
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_proxy_credentials():
    proxies = [
        '93.180.134.114:45785',
        '87.251.2.8:45785',
        '87.251.18.73:45785',
        '87.251.16.145:45785',
        '87.251.2.253:45785',
        '87.251.18.71:45785',
        '87.251.18.6:45785',
        '87.251.2.175:45785',
        '87.251.18.34:45785',
    ]
    proxy = random.sample(proxies, 1)[0]
    proxy_tokens = proxy.split(':')
    hostname = proxy_tokens[0]
    port = proxy_tokens[1]
    proxy_username = "Selnagmat"
    proxy_password = "V5i2TaT"
    return proxy_username, proxy_password, hostname, port


def get_vfs_login_credentials():
    return "nagi@mailna.in", "Nagi@1234"  # TODO


def vfs_login_page():
    wait.until(EC.presence_of_element_located((By.ID, 'mat-input-0')))
    email_field = driver.find_element(by=By.ID, value='mat-input-0')
    password_field = driver.find_element(by=By.ID, value='mat-input-1')
    email, password = get_vfs_login_credentials()
    email_field.send_keys(email)
    password_field.send_keys(password)
    email_field.send_keys(Keys.RETURN)


def clickable_element(identifier, sleep_time):
    wait.until(EC.presence_of_element_located(identifier))
    wait.until(EC.element_to_be_clickable(identifier))
    time.sleep(sleep_time)
    driver.find_element(identifier[0], identifier[1]).click()


def check_available_bookings(name, trial):
    try:
        # Click the first dropdown
        clickable_element((By.ID, "mat-select-0"), 2)
        clickable_element((By.XPATH, f"//span[@class='mat-option-text'][contains(text(),'{name}')]"), 2)
        # Click the second dropdown
        clickable_element((By.ID, "mat-select-2"), 2)
        clickable_element((By.XPATH, "//span[contains(text(),'National Visa (Type D)')]"), 2)
        # Third dropdown
        clickable_element((By.ID, "mat-select-4"), 2)
        # clickable_element((By.XPATH, "//span[contains(text(),'Foreigners')]"), 2)
        clickable_element((By.XPATH, "//span[contains(text(),'Education')]"), 2)
    except:
        if trial == 3:
            print(f"Three trials have been done for {name}, going to the next one")
            return
        print(f"Retry No.{trial} for {name} due to an error")
        check_available_bookings(name, trial + 1)


def fill_information_page():
    import csv
    print("Fill information page")
    lines = []
    with open('list.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    # print("data = ", data)
    # print("data[0]",data[0])
    adam = data[0]

    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.ID, 'mat-input-2')))
    name_field = driver.find_element(by=By.ID, value='mat-input-2')
    surname_field = driver.find_element(by=By.ID, value='mat-input-3')
    name_field.send_keys(adam[0])
    surname_field.send_keys(adam[1])
    clickable_element((By.ID, "mat-select-6"), 2)
    clickable_element((By.XPATH, f"//span[@class='mat-option-text'][contains(text(),'{adam[2]}')]"), 2)
    dob = driver.find_element(by=By.ID, value='dateOfBirth')
    dob.send_keys(adam[3])
    clickable_element((By.ID, "mat-select-8"), 2)
    clickable_element((By.XPATH, f"//span[@class='mat-option-text'][contains(text(),'{adam[4]}')]"), 2)
    wait.until(EC.presence_of_element_located((By.ID, 'mat-input-4')))
    passno = driver.find_element(by=By.ID, value='mat-input-4')
    passno.send_keys(adam[5])
    wait.until(EC.presence_of_element_located((By.ID, 'passportExpirtyDate')))
    passexp = driver.find_element(by=By.ID, value='passportExpirtyDate')
    passexp.send_keys(adam[6])
    wait.until(EC.presence_of_element_located((By.ID, 'mat-input-5')))
    telno1 = driver.find_element(by=By.ID, value='mat-input-5')
    telno1.send_keys(adam[7])
    wait.until(EC.presence_of_element_located((By.ID, 'mat-input-6')))
    telno2 = driver.find_element(by=By.ID, value='mat-input-6')
    telno2.send_keys(adam[8])
    wait.until(EC.presence_of_element_located((By.ID, 'mat-input-7')))
    emailid = driver.find_element(by=By.ID, value='mat-input-7')
    emailid.send_keys(adam[9])

    clickable_element((By.XPATH, "//span[normalize-space()='Save']"), 2)


def booking_page():
    ls = ["Beyoglu", "Izmir", "Gaziantep", "Trabzon"]
    while True:
        try:
            for name in ls:
                check_available_bookings(name, 0)
                time.sleep(2)
                text = driver.find_element(By.XPATH, "//div[@class='alert alert-info border-0 rounded-0']").text
                if "No appointment" in text:
                    print("No Appointments :(")
                    continue
                else:
                    time.sleep(5)
                    clickable_element((By.XPATH, "//span[normalize-space()='Continue']"), 2)
                    return
        except Exception as e:
            print(getattr(e, 'message', repr(e)))


def proxy_login_page(tokens):
    time.sleep(2)
    pyautogui.typewrite(tokens[0])
    pyautogui.press('tab')
    pyautogui.typewrite(tokens[1])
    pyautogui.press('enter')


def check_the_ip():
    import socket
    print(f"My IP before the proxy is {socket.gethostbyname(socket.gethostname())}")
    driver.execute_script("window.open('http://ipinfo.io/ip')")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    proxy_ip = driver.find_element(By.XPATH, "//body").text
    print(f"Prox IP is {proxy_ip}")
    driver.execute_script("window.close()")
    driver.switch_to.window(driver.window_handles[0])


def get_chrome_options():
    chrome_options = Options()
    software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value]
    os = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.IOS.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=os, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    ip = "94.23.241.200"
    port = "3128"
    chrome_options.add_argument(f'--proxy-server={tokens[2]}:{tokens[3]}')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument(f'--user-agent={user_agent}')
    return chrome_options


if __name__ == "__main__":
    tokens = get_proxy_credentials()
    ch_opt = get_chrome_options()
    url = "https://visa.vfsglobal.com/tur/en/pol/login"
    # driver = webdriver.Chrome(options=ch_opt, executable_path='/home/nnazarov/chromedriver')
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.set_window_size(1200, 800)
    driver.set_window_position(0, 0)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.get(url)
    proxy_login_page(tokens[0:2])
    wait = WebDriverWait(driver, 60)
    # check_the_ip()
    clickable_element((By.XPATH, "//button[normalize-space()='Reject All']"), 3)
    vfs_login_page()
    # Start New Booking button
    clickable_element((By.XPATH, "/html/body/app-root/div/app-dashboard/section/div/div[2]/button"), 2)
    # clickable_element((By.XPATH, "//span[normalize-space()='Start New Booking']"), 3)
    booking_page()
    fill_information_page()
    #######################################33
    clickable_element((By.XPATH, "//span[normalize-space()='Continue']"), 2)
    time.sleep(3)
    driver.find_element(By.XPATH, "//td[contains(@class, 'date-availiable')]").click()
    driver.find_element(By.XPATH, "//input[@id='STRadio1']").click()
    clickable_element((By.XPATH, "//span[normalize-space()='Continue']"), 2)
    driver.find_element(By.XPATH, "//label[@for='mat-checkbox-1-input']").click()
    driver.find_element(By.XPATH, "//label[@for='mat-checkbox-2-input']").click()
    clickable_element((By.XPATH, "//span[normalize-space()='Pay Online']"), 2)