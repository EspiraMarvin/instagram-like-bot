from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # firefox browser driver
        self.bot = webdriver.Firefox(executable_path='C:/Users/user/Downloads/geckodriver-v0.28.0-win64/geckodriver.exe')
        # chrome browser driver
        # self.bot =  webdriver.Chrome(executable_path='C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com/accounts/login')
        time.sleep(3)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        time.sleep(3)

    # search hashtags
    def searchHashtag(self, hashtag):
        bot = self.bot

        bot.get('https://www.instagram.com/explore/tags/' + hashtag)

    # like photos
    def likePhotos(self, amount):
        bot = self.bot
        bot.find_element_by_class_name('_9AhH0').click()

        i = 1
        while 1 <= amount:
            # bot.find_element_by_class_name("FY9nT").click()
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            # bot.find_element_by_class_name('coreSpriteRightChevron').click()
            time.sleep(5)

            i += 1

        # time.sleep(100)
        # bot.get('https"//instagram.com' + self.username)


insta = InstagramBot('your username', 'your password')
insta.login()
insta.searchHashtag('cars')
# insta.searchHashtag('travel')
insta.likePhotos(5)
