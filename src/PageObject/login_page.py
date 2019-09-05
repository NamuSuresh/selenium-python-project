from src.PageObject.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_CONTAINER = 'email'
    PASSWORD_CONTAINER = 'passwd'
    SUBMIT_BUTTON = 'SubmitLogin'


    def set_emailId(self, email_id:str):
        self._driver.find_element_by_id(LoginPage.EMAIL_CONTAINER).send_keys(email_id)

    def set_password(self, password:str):
        self._driver.find_element_by_id(LoginPage.PASSWORD_CONTAINER).send_keys(password)

    def set_signIn(self):
        self._driver.find_element_by_id(LoginPage.SUBMIT_BUTTON).click()


    def check_page_source(self, value):
        return value in self._driver.page_source


    def set_credentials(self, email_id, password):
        self.set_emailId(email_id)
        self.set_password(password)
        self.set_signIn()

