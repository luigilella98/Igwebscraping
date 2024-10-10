from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def Check():
        try:
            driver.find_element_by_class_name("Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.HVWg4")
            return 1
        except:
            return 0   

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def Login(self):
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='Consenti solo i cookie essenziali']").click()
        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(3)
        driver.find_element_by_class_name('Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB').click()
        time.sleep(8)

    def openStories(self):
        amici = 0
        driver.get("https://www.instagram.com/nomeutente/") #MODIFICA QUESTO CON IL NOME DELL'ACCOUNT 
        time.sleep(2)
        driver.find_element_by_class_name('NCYx-').click()
        time.sleep(5)
        while "highlights" in driver.current_url:
            if Check() != 0:
                print("SEI TRA GLI AMICI PIU' STRETTI")
                amici = 1
                break
            else:
                driver.find_element_by_class_name("coreSpriteRightChevron").click()
        
        if amici == 0:
            print("FORSE QUESTA PERSONA TI HA TOLTO DAGLI AMICI PIU' STRETTI :(")


driver = webdriver.Firefox(executable_path=r'C:\Users\luigi\Downloads\geckodriv\geckodriver.exe')
go = InstaBot('user','psw') #MODIFICA QUESTO CON USERNAME E PASSWORD
go.Login()
go.openStories()