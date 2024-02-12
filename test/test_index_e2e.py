import unittest
from selenium import webdriver


class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\\Users\\pacquier\\PycharmProjects\\chromedriver_win32\\chromedriver.exe")
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

