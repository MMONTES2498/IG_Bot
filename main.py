from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome('/Users/Downloads/chromedriver')
        self.email = email
        self.password = password

    def signIn(self):
        browser = self.browser
        browser.get("https://www.instagram.com/")
        time.sleep(2)

        emailInput= browser.find_element(By.NAME,"username")
        passwordInput = browser.find_element(By.NAME,"password")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

        browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div/div/div/button").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div[3]/button[2]").click()

bot = InstagramBot("insert username", "insert password")
bot.signIn()
