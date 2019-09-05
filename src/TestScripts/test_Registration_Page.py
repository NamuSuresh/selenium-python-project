import unittest
from src.PageObject.home_page import HomePage
from src.PageObject.login_page import LoginPage
from src.PageObject.registration_page import SignUp
from time import sleep
from TestBase.test_template import TestTemplate
from selenium.webdriver.common.action_chains import ActionChains


class TestRegistration(TestTemplate):

    def test_RegistrationFlow(self):
        home_page = HomePage(self.driver)
        home_page.signin()
        sleep(3)
        sign_up = SignUp(self.driver)
        element = self.driver.find_element_by_id(SignUp.SUBMIT_CREATE)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(3)

        if (sign_up.reg_button()):
            print("Registration form is available")
            sign_up.set_email('namu224@test.com')
            sign_up.signup()
            sleep(3)
        else:
            print("Registration Form not loaded")

        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sign_up.set_title()
            sign_up.set_firstName('Tata')
            sign_up.set_lastName('Birla')
            sign_up.set_passWord('toyota123%')
            sign_up.set_dOB('7')
            sign_up.set_mOB('12')
            sign_up.set_yOB('2000')
            sign_up.set_newsLetter()
            sign_up.set_splOffers()
            sign_up.set_company('iBaco')
            sign_up.set_address1('21, tuttudoo apartment')
            sign_up.set_address2('Baywatch road')
            sign_up.set_city('Mountain View')
            sign_up.set_state('5')
            sign_up.set_zipCode('94040')
            sign_up.set_additional_info('Nothing for now')
            sign_up.set_mobilePhone('9173544551')
            sign_up.set_aliasAddress('N/a')
            sign_up.register()
            sleep(3)

        except Exception as e:
            print('Exception occurred' + e)


        if (sign_up.result()):
            login = LoginPage(self.driver)
            assert login.check_page_source("Welcome to your account.")
            print("Registration Process Successful")
        else:
            print('User failed to register properly')


if __name__ == '__main__':
    unittest.main()
