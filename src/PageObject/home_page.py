from src.PageObject.base_page import BasePage

class HomePage(BasePage):
    SIGNIN_MENU = 'login'
    CONTACT_US = 'contact-link'
    SEARCH = 'submit_search'
    SEARCH_INPUT ='search_query_top'

    def check_signin(self):
        return self._driver.find_element_by_class_name(HomePage.SIGNIN_MENU).is_displayed()

    def signin(self):
        self._driver.find_element_by_class_name(HomePage.SIGNIN_MENU).click()

    def check_contact(self):
        return self._driver.find_element_by_id(HomePage.CONTACT_US).is_displayed()

    def contact_us(self):
        self._driver.find_element_by_id(HomePage.CONTACT_US).click()

    def set_search_query(self, query: str):
        self._driver.find_element_by_id(HomePage.SEARCH_INPUT).send_keys(query)

    def check_search(self):
        return self._driver.find_element_by_name(HomePage.SEARCH).is_displayed()

    def search(self):
        self._driver.find_element_by_name(HomePage.SEARCH).click()

    def check_page_source(self, value):
        return value in self._driver.page_source



