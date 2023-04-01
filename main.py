# faintt#1150

from selenium.webdriver.common import keys
from random_username.generate import generate_username
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from colorama import Fore
import time
import os
import random

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

print(Fore.LIGHTMAGENTA_EX,'''
 █████╗ ██╗  ████████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██║  ╚══██╔══╝██╔════╝ ██╔════╝████╗  ██║
███████║██║     ██║   ██║  ███╗█████╗  ██╔██╗ ██║
██╔══██║██║     ██║   ██║   ██║██╔══╝  ██║╚██╗██║
██║  ██║███████╗██║   ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝
            coded by faintt#1150\n                              
''')

driver = webdriver.Chrome(options=options)
driver.get('https://roblox.com/')

def main():
    elem = driver.find_elements(By.XPATH, '//*[@id="signup-username"]')
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signup-username"]'))).clear()

    birthmonth = driver.find_elements(By.XPATH, '//*[@id="MonthDropdown"]')
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MonthDropdown"]'))).click()

    jan = driver.find_elements(By.XPATH, '//*[@id="MonthDropdown"]/option[2]')
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MonthDropdown"]/option[2]'))).click()

    day = driver.find_elements(By.XPATH, '//*[@id="DayDropdown"]')
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DayDropdown"]'))).click()

    num = driver.find_elements(By.XPATH, '//*[@id="DayDropdown"]/option[2]')
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DayDropdown"]/option[2]'))).click()

    year = driver.find_elements(By.XPATH, '//*[@id="YearDropdown"]')
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="YearDropdown"]'))).click()

    num1 = driver.find_elements(By.XPATH, '//*[@id="YearDropdown"]/option[38]')
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="YearDropdown"]/option[38]'))).click()


    digits = [str(random.randint(0, 9)) for _ in range(10)]
    username = f'faint'+''.join(digits)
    password = f''.join(digits)

    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signup-username"]'))).send_keys(username)

    time.sleep(2)

    # check if username valid
    checker = driver.find_elements(By.ID, 'signup-usernameInputValidation')
    text = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, 'signup-usernameInputValidation'))).get_attribute('textContent')
    time.sleep(0.5)

    def check():
        if text == "This username is already in use." or "Username not appropriate for Roblox.":
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signup-username"]'))).clear()
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signup-username"]'))).send_keys(username)

    passs = password
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signup-password"]'))).send_keys(passs)

    # double check again
    if len(text) > 1:
        check()

    sign = driver.find_elements(By.XPATH, '//*[@id="signup-button"]')
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signup-button"]'))).click()
    os.system('cls')

    try:
        # wait for captcha to finish and then log the cookie
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="FunCaptcha"]')))
        WebDriverWait(driver, 1).until_not(EC.presence_of_element_located((By.XPATH, '//*[@id="FunCaptcha"]')))
    except TimeoutException:
        pass

    combo = username+':'+password 
    with open('alts.txt', 'a') as alts:
        alts.write(f"{combo}\n")
        alts.close()
    print('[#] Combo Saved')
    driver.get('https://www.roblox.com/')
    time.sleep(1)
    main()

if __name__ == "__main__":
    main()