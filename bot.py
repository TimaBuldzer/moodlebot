from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ModdleBot:

    def __init__(self, uname, passw):
        self.uname = uname
        self.passw = passw
        self.driver = webdriver.Chrome()
    
    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("http://moodle.ubtuit.uz/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//*[@id='page-wrapper']/nav/ul[2]/li[2]/div/span/a")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.uname)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.passw)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def checkIn(self):
        time.sleep(2)
        driver = self.driver
        pageCnt = 5
        while pageCnt < 14:

            try:
                formatted = "//*[@id='nav-drawer']/nav/a[{}]".format(pageCnt)
                subject = driver.find_element_by_xpath(formatted)
                subject.click()
                time.sleep(2)
                driver.get("http://moodle.ubtuit.uz/")
                time.sleep(2)
                pageCnt+=1
            except:
                print("Закончились страницы")
                break
        print(f"Courses viewed: {pageCnt - 5}, Everything is fine.")

#b19011 sardorthebest
inp = input("Enter your name: ")

if inp == "Timur":
    username = "b19014"
    password = "b19014"
    
Tim = ModdleBot(username, password)

Tim.login()
Tim.checkIn()
Tim.closeBrowser()