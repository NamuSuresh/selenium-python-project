from src.PageObject.home_page import HomePage
from TestBase.test_template import TestTemplate
from src.PageObject.login_page import LoginPage


class TestLoginPage(TestTemplate):

    def test_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namutest46@gmail.com', 'test@1234')
        assert login.check_page_source("Welcome to your account.")

    def test_invalid_email(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namu46@gmail.com', 'test@1234')
        assert login.check_page_source("Authentication failed.")

    def test_single_letter_email(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('n', 'test@1234')
        assert login.check_page_source("Invalid email address.")

    def test_empty_password(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('NotjustagreatvalleybutashrinetohumanforesightthestrengthofgranitethepowerofglaciersthepersistenceoflifeandthetranquilityoftheHighSierraFirst protectedin1864YosemiteNationalParkisbestknownforitswaterfallst@gmail.com', 'test@1234')
        assert login.check_page_source("Authentication failed.")

    def test_email_with_space(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namu test46@gmail.com', 'test@1234')
        assert login.check_page_source("Invalid email address.")

    def test_email_missing_symbol(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namutest46gmail.com', 'test@1234')
        assert login.check_page_source("Invalid email address.")


    def test_missing_dot_email(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namutest46@gmailcom', 'test@1234')
        assert login.check_page_source("Invalid email address.")

    def test_symbol_added_email(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namu#@$test46@gmail.com', 'test@1234')
        assert login.check_page_source("Invalid email address.")


    def test_missing_symbol_password(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namutest46@gmail.com', 'test1234')
        assert login.check_page_source("Authentication failed.")


    def test_single_letter_password(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namutest46@gmail.com', 't')
        assert login.check_page_source("Invalid password.")

    def test_max_length_password(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namutest46@gmail.com', 'tNotjustagreatvalleybutashrinetohumanforesightthestrengthofgranitethepowerofglaciersthepersistenceoflifeandthetranquilityoftheHighSierraFirst')
        assert login.check_page_source("Authentication failed.")

    def test_empty_email(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('', 'test@1234')
        assert login.check_page_source("An email address required.")

    def test_space_email(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials(' ', 'test@1234')
        assert login.check_page_source("An email address required.")

    def test_space_password(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namutest46@gmail.com', ' ')
        assert login.check_page_source("Password is required.")

    def test_empty_password(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namutest46@gmail.com', '')
        assert login.check_page_source("Password is required.")

    def test_space_between_email(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namu test46@gmail.com', 'test@1234')
        assert login.check_page_source("Invalid email address.")

    def test_space_between_password(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        login = LoginPage(self.driver)
        login.set_credentials('namutest46@gmail.com', 'test @1234')
        assert login.check_page_source("Authentication failed.")





