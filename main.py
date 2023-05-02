#LINKEDIN POSTS AUTOMATION USING SELENIUM

#Import dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

#webdriver path
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=r"C:\Users\jayes\Downloads\chromedriver_win32\chromedriver.exe"))

#LinkedIn URL for log-in
url='https://www.linkedin.com/home'
driver.get(url)
time.sleep(2)

#get input field for signing in
email=driver.find_element("xpath", "//input[@name = 'session_key']")
password=driver.find_element("xpath", "//input[@name = 'session_password']")

#getting username and password
with open(r"C:\Users\jayes\Desktop\usernameforLI.txt") as myInfo:
    username=myInfo.read().replace('\n', '')
email.send_keys(username)

with open(r"C:\Users\jayes\Desktop\passwordLI.txt") as myPass:
    passc=myPass.read().replace('\n', '')
password.send_keys(passc)
time.sleep(2)

# sign in button
signin=driver.find_element("xpath", '//button[@type = "submit"]').click()
time.sleep(2)

#create a post button
postarticle = driver.find_element("xpath", '//span[text() = "Start a post"]').click()
time.sleep(10)


