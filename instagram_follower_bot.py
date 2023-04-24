import time
from instafollow import InstaFollower
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

CHROME_DRIVER_PATH = "C:\chromedriver_win32\chromedriver.exe"
USERNAME = INSERT_USERNAME
PASSWORD = INSERT_PW
SUCHE = INSERT_SEARCHING


class Twitterbot:

    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.chrome_driver = webdriver.Chrome()

        chrome_driver_path = CHROME_DRIVER_PATH
        s = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=s)
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)

    def login(self):
        #time.sleep(300)
        time.sleep(2)
        cookies = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        cookies.click()
        time.sleep(2)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        anmelden = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
        anmelden.click()
        time.sleep(5)
        benachrichtung = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        benachrichtung.click()
        print("F")

    def find_followers(self):
        suche = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div')
        suche.click()
        time.sleep(2)
        suche_suche = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        suche_suche.send_keys(SUCHE)
        time.sleep(2)
        suche_stichwort = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a')
        suche_stichwort.click()
        time.sleep(3)
        follower_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        follower_button.click()
        time.sleep(3)


    def follow(self):
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        scr1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for x in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(1)
        all_buttons = self.driver.find_elements(By.XPATH, "//button[contains(.,'Folgen')]")
        print(all_buttons)
        print(len(all_buttons))

        for button in all_buttons:
            self.driver.execute_script("arguments[0].click();", button)
            time.sleep(2)
        time.sleep(300)


twitterbot = Twitterbot()
twitterbot.login()
twitterbot.find_followers()
twitterbot.follow()