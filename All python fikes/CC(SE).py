from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class CookieBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        time.sleep(1)
        cookie = self.driver.find_element_by_id('bigCookie')
        while True:
            cookie.click()
            try:
                product = self.driver.find_element_by_class_name('product.unlocked')
                product.click()
##            self.driver.find_element_by_xpath("//div[@class=product unlocked enabled]").click()
##            self.driver.find_element_by_xpath("/html/body/div/div[2]/div[15]/div[8]/div[1]").click()
            except NoSuchElementException:
                print("You don't have enough cookies to buy that!")
            continue
            try:
                upgrade = self.driver.find_element_by_class_name('crate upgrade')
                upgrade.click()
            except NoSuchElementException:
                print("Insufficient Funds")
            continue


CookieBot()