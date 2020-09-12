# 2020-09-06 - 2020-09-08 (Utvecklingsstadie fortfarande)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from secrets import pw as pw
from time import sleep
from datetime import datetime



#class Webbot:
#    def __init__(self, username, pw):
#        self.username = username
#        self.pw = pw
#        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
#        self.driver.get("Https://instagram.com")
#        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
#        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.pw)
#        sleep(15)

class Weblamp:
    def __init__(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        self.lamps = 0
        # self.driver.get("http://10.0.0.11/")
        # sleep(0.005)

    def Stairs_Gr_Tv(self):
        self.driver.get("http://10.0.0.11/")
        self.driver.find_element_by_xpath('/html/body/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="stairs.s"]').click()
        self.lamps += 1
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="gabrielsrum.s"]').click()
        self.lamps += 1
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="tv_uppe.s"]').click()
        self.lamps += 1
        self.driver.quit()
        print(f"Totalt tände/släckte jag {self.lamps}")
        with open("Webscraper.txt", "a") as file:
            file.write(f"\n{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} Totalt tändes/släcktes {self.lamps} lampor \n")

    def ReturnLamps(self):
        return self.lamps

    def Downstairs(self):
        pass

first = input("Vill du tända/släcka Trappan (Lådorna på väggen) Tvn och ditt rum, Y / N \n")




if(first == "Y" or first == " Y"):
    print("\nDetta kommer ta ca 1-15 sekund(er) att genomföra. Vänligen vänta")
    Weblamp().Stairs_Gr_Tv()
    dots = [".", "..", "..."]
    print(dots[0])
    sleep(1.25)
    print(dots[1])
    print(dots[2])
else:
    exit()
