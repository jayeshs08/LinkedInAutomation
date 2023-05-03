from selenium import webdriver
import time
import pandas as pd
#import os

from selenium.webdriver.support.select import Select  #selects html elements
from selenium.webdriver.support.ui import WebDriverWait #tool for creating web automation scripts to handle dynamic asynchronus content
from selenium.webdriver.common.by import By #to locate web elements on a web page eg By ID,NAME,CLASS_NAME,XPATH etc

#linkdIn post page
url1= 'https://www.linkedin.com/jobs/search/?currentJobId=3594599677&f_E=1&f_JT=I&f_TPR=r604800&geoId=102713980&keywords=Jobs&location=India'
#url1= 'https://www.linkedin.com/jobs/search?keywords=Jobs&location=India&locationId=&geoId=102713980&f_TPR=r2592000&f_JT=I%2CF&f_E=1&position=1&pageNum=0'
#linking chrome driver
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=r"C:\Users\DELL\Downloads\chromedriver_win32\chromedriver.exe"))

driver.get(url1)
time.sleep(5)

#this would fetch the number of jobs available
n = driver.find_elements(By.CLASS_NAME, 'results-context-header__job-count')[0].text
y=pd.to_numeric(n)

#instructing python to keep scrolling and then clicking see more jobs if it arrives
i=2
while(i<5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    i=i+1
    try:
        x=driver.find_element(By.XPATH, '//button[@aria-label = "See more jobs"]')
        driver.execute_script("arguments[0].click();", x)
        time.sleep(10)
    except:
        pass
        time.sleep(2)