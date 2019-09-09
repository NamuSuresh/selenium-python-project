from src.PageObject.home_page import HomePage
from TestBase.test_template import TestTemplate
from time import sleep


class TestHomePage(TestTemplate):

    def test_signin_menu_available(self):
        main_page = HomePage(self.driver)
        assert main_page.check_signin()

    def test_signin_click(self):
        main_page = HomePage(self.driver)
        main_page.signin()
        sleep(2)
        assert main_page.check_page_source("Authentication")

    def test_contact(self):
        main_page = HomePage(self.driver)
        assert main_page.check_contact()

    def test_contact_click(self):
        main_page = HomePage(self.driver)
        main_page.contact_us()
        sleep(2)
        assert main_page.check_page_source("Customer service - Contact us")

    def test_check_search(self):
        main_page = HomePage(self.driver)
        assert main_page.check_search()

    def test_search(self):
        main_page = HomePage(self.driver)
        main_page.search()
        sleep(2)
        assert main_page.check_page_source("Search")





