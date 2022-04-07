import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass

# Init:
gecko_path = '/usr/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)

url = 'http://campuswire.com/signin'

# Actual program:
driver.get(url)

time.sleep(2)

username = driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
my_email = input('Please provide your email:')
username.send_keys(my_email)

time.sleep(5)

password = driver.find_element(By.XPATH, '//input[@placeholder="password"]')
my_pass = getpass.getpass('Please provide your password:')
password.send_keys(my_pass)
time.sleep(5)

button = driver.find_element(By.XPATH, '//button[@type="submit"]')
button.click()

time.sleep(7)

chat = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/aside[1]/div/div[1]/ul/li[2]/button')
chat.click()

time.sleep(7)

bot_test_chat = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/aside[2]/div[3]/ul/li[1]/div[2]/h5')
bot_test_chat.click()

time.sleep(5)


selector = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/button[1]/input')
selector.send_keys("/home/qehremanekber/class_7/ex_1.py")
time.sleep(5)