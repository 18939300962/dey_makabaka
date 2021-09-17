from selenium import webdriver
from xue_001.lianxi001.basepage import Basepage
from time import sleep
from selenium.webdriver.common.by import By
class ymfz(Basepage):
    bd_loc1 = (By.ID,"kw")
    bd_loc5 = (By.ID,"su")
    def dkwz_01(self):
        self.driver = webdriver.Firefox()
        self.dkwz("https://www.baidu.com/")
        sleep(1)
    def sunr(self):
        self.shur(*self.bd_loc1,"迪迦")
        sleep(1)
    def djss(self):
        self.dj(*self.bd_loc5)
# fs = ymfz(Basepage)
# fs.dkwz_01()
# fs.sunr()
# fs.djss()