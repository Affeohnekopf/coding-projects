from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()

chrome_driver_path = "C:\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url='https://orteil.dashnet.org/cookieclicker/'
driver.get(url)

time.sleep(2)
button_accept = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]')
button_accept.click()
time.sleep(2)
button_en = driver.find_element(By.ID, 'langSelect-EN')
button_en.click()
time.sleep(3)
button_cookie = driver.find_element(By.ID, 'bigCookie')

# Products
product0 = driver.find_element(By.ID, 'product0')
product1 = driver.find_element(By.ID, 'product1')
product2 = driver.find_element(By.ID, 'product2')
product3 = driver.find_element(By.ID, 'product3')
product4 = driver.find_element(By.ID, 'product4')
product5 = driver.find_element(By.ID, 'product5')


timeout = time.time() + 5
time_end = time.time() + (5 * 60)

while True:
    button_cookie.click()
    cookies_count = driver.find_element(By.ID, 'cookies').text.split()
    cookies_count = int(cookies_count[0])
    if time.time() >= timeout:
        try:
            product0_price = int(driver.find_element(By.ID, 'productPrice0').text)
        except ValueError:
            product0_price = 10000000
        try:
            product1_price = int(driver.find_element(By.ID, 'productPrice1').text)
        except ValueError:
            product1_price = 10000000
        try:
            product2_price = int(driver.find_element(By.ID, 'productPrice2').text)
        except ValueError:
            product2_price = 10000000
        try:
            product3_price = int(driver.find_element(By.ID, 'productPrice3').text)
        except ValueError:
            product3_price = 10000000
        try:
            product4_price = int(driver.find_element(By.ID, 'productPrice4').text)
        except ValueError:
            product4_price = 10000000
        try:
            product5_price = int(driver.find_element(By.ID, 'productPrice5').text)
        except ValueError:
            product5_price = 10000000

        if cookies_count > product5_price:
            product5.click()
            timeout = time.time() + 5
        elif cookies_count > product4_price:
            product4.click()
            timeout = time.time() + 5
        elif cookies_count > product3_price:
            product3.click()
            timeout = time.time() + 5
        elif cookies_count > product2_price:
            product2.click()
            timeout = time.time() + 5
        elif cookies_count > product1_price:
            product1.click()
            timeout = time.time() + 5
        elif cookies_count > product0_price:
            product0.click()
            timeout = time.time() + 5
    if time.time() >= time_end:
        print(driver.find_element(By.ID, 'cookiesPerSecond').text)
        break

