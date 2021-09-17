import unittest
from selenium import webdriver
from time import sleep
from xue_001.lianxi001.searchpage import ymfz

class baidu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        sleep(1)
    def tearDown(self) -> None:
        self.driver.quit()
    def test_001(self):
        po = ymfz(self.driver)
        po.dkwz_01()
        sleep(1)
        po.sunr()
        sleep(1)
        po.djss()
        sleep(1)
if __name__ == '__main__':
    unittest.main(verbosity=2)

