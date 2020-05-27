from selenium import webdrvier
import time

class instabot():
	def __init__(self, user, pw, usern):
		self.driver = webdriver.Chrome(
			executable_path=r'C:\Users\galbers\Documents\Pycharm Projects\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
		self.driver.get("https://instagram.com")
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        time.sleep(2)
        loginfield = self.driver.find_element_by_xpat7h(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        loginfield.send_keys(user)
        passfield = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        passfield.send_keys(pw)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

        time.sleep(1)

        searchbar = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        searchbar.send_keys(usern)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a').click()
        time.sleep(1.5)


    def get_unfollowers(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self.get_names()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self.get_names()
        not_following_back = [user for user in following if user not in followers]
        not_following = [user for user in followers if user not in following]
        print("People you aren't following: ", not_following)
        print("People that aren't following you: ", not_following_back)

##  GET NAMES
    def get_names(self):
        time.sleep(0.5)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(0.5)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]').click()
        return names



iBot = instabot("gustavalbers", "gustav923", "brianna.simington")