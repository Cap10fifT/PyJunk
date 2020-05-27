from selenium import webdriver
import time


class InstaBot():
    def __init__(self, user, pw):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\galbers\Documents\Pycharm Projects\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
        )
        self.driver.get("https://instagram.com")
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        time.sleep(2)
        loginfield = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        loginfield.send_keys(user)
        passfield = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        passfield.send_keys(pw)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()

        time.sleep(1)



    def GoToFollowStaff(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self.get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'followers')]").click()
        followers = self.get_names()

    def get_names(self):
        time.sleep(1.2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(0.8)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]').click()
        x = 1
        for name in names:
            searchbar = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
            searchbar.send_keys(name)
            time.sleep(2.4)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a/div/div[2]/div/span').click()
            time.sleep(1.2)
            accfollers =  self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").get_attribute("title")

##            searchbar.send_keys(Keys.BACKSPACE)
            time.sleep(1)
            print(name, accfollers)




iBot = InstaBot("gustavalbers", "gustava923")
iBot.GoToFollowStaff()