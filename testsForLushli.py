from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

class TestLushliWebExistanceOftheElemnts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/andrii/Downloads/chromedriver_mac64/chromedriver')

    def test_ExistanceOfSearchfield(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        #screenshot = driver.find_element_by_name('mail').screenshot_as_png
        assert driver.find_element_by_name('mail')

    def test_ExistanceOfLowerImages(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        #screenshot = driver.find_element_by_id("challenge-part").screenshot_as_png
        assert driver.find_element_by_id("challenge-part")

    def test_ExistanceOfTheLogo(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        #screenshot = driver.find_element_by_class_name('challenge__header').screenshot_as_png
        assert driver.find_element_by_class_name('challenge__header')

    def test_ExistanceOfTheLandingPhoto(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        #screenshot = driver.find_element_by_xpath('// *[ @ id = "challenge-part"] / div / aside[1]').screenshot_as_png
        assert driver.find_element_by_xpath('// *[ @ id = "challenge-part"] / div / aside[1]')


    def test_CorrectnessOfTheUpperText(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        text = driver.find_element_by_xpath('//*[@id="challenge-part"]/div/aside[2]/section/article[1]/h1/strong').text
        #print(text)
        assert text[ : 72] == "Enter the #askINKEYchallenge for the chance to win one of The INKEY List"

    def test_CorrectnessOfTheMiddleText(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        text = driver.find_element_by_xpath(
            '//*[@id="challenge-part"]/div/aside[2]/section/article[1]/p[1]/strong').text
        #print(text)
        assert text[ : 14] == "The INKEY List"

    def test_CorrectnessOfTheSighnInText(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        text = driver.find_element_by_xpath(
            '//*[@id="challenge-part"]/div/aside[2]/section/article[2]/div[1]/p').text
        #print(text)
        assert text == "Sign in using your Instagram & provide your email"

    def test_CorrectnessOfTheLowestText(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        text = driver.find_element_by_xpath(
            '// *[ @ id = "challenge-part"] / div / aside[2] / section / article[1] / p[2]').text
        #print(text)
        assert text[: 43] == "To celebrate their US launch at Sephora, we"

    def test_CorrectnessOfTheChallegeText(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        text = driver.find_element_by_xpath(
           '//*[@id="challenge-part"]/div/aside[2]/section/article[2]/div[2]/p').text
        #print(text)
        assert text == "For the chance to win even more, post your best product shot or selfie on Instagram asking a question about your product ingredient,, tagging @theinkeylist #askINKEYchallenge. One grand prize winner will receive a $1,000 Sephora gift card and two runner ups will receive $500!"

    def tearDown(self):
        self.driver.close()


class TestLushliSearchFieldandLinkProperWork(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/andrii/Downloads/chromedriver_mac64/chromedriver')

    def test_ExistanceOfWarning(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        driver.find_element_by_name('mail').send_keys('test@test.com')
        driver.find_element_by_id("login").click()
        time.sleep(5)
        assert driver.find_element_by_id('warning')


    def test_PopsitiveofLogIN(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        driver.find_element_by_id("follow-checkbox").click()
        driver.find_element_by_name('mail').send_keys('test@test.com')
        driver.find_element_by_id("login").click()
        time.sleep(5)
        assert driver.find_element_by_id('react-root')

    def test_NegativeofLogIN(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        driver.find_element_by_id("follow-checkbox").click()
        driver.find_element_by_name('mail').send_keys('test')
        driver.find_element_by_id("login").click()
        alert = driver.switch_to.alert
        alert.accept()
        assert driver.find_element_by_id("login")

    def test_TermsAndConditions(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        link = driver.find_element_by_xpath(
        '//*[@id="challenge-part"]/div/aside[2]/section/article[2]/div[1]/form/label/a')
        url = link.get_attribute("href")
        assert url == 'https://www.preen.me/c/theinkeylisttandc#/'

    def test_TermsAndConditionsTransfer(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        link = driver.find_element_by_xpath(
        '//*[@id="challenge-part"]/div/aside[2]/section/article[2]/div[1]/form/label/a')
        link.click()
        time.sleep(8)
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == 'https://www.preen.me/c/theinkeylisttandc#/'

    def test_TermsAndConditionsTransferBack(self):
        driver = self.driver
        driver.get('https://lushli.com/theinkeylist/')
        link = driver.find_element_by_xpath(
        '//*[@id="challenge-part"]/div/aside[2]/section/article[2]/div[1]/form/label/a')
        link.click()
        time.sleep(8)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(8)
        driver.switch_to.window(driver.window_handles[0])
        #print(driver.current_url)
        assert driver.current_url == 'https://lushli.com/theinkeylist/'

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



