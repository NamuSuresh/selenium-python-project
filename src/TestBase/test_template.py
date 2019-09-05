import unittest
from selenium import webdriver

class TestTemplate(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("/Users/Namusuresh/Selenium/TestProject/Drivers/chromedriver")
        self.driver.get('http://automationpractice.com/index.php')

    def tearDown(self):
        self.driver.quit()
