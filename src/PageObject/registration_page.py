from selenium.webdriver.support.select import Select

from src.PageObject.base_page import BasePage


class SignUp(BasePage):
    EMAIL_ID ='email_create'
    SUBMIT_CREATE = 'SubmitCreate'
    TITLE ='id_gender2'
    FIRST_NAME = 'customer_firstname'
    LAST_NAME = 'customer_lastname'
    PASSWORD = 'passwd'
    DAY = 'days'
    MONTH = 'months'
    YEAR = 'years'
    NEWS_LETTER = 'newsletter'
    OFFERS = 'optin'
    ADDRESS_FN = 'firstname'
    ADDRESS_LN = 'lastname'
    COMPANY = 'company'
    ADDRESS1 = 'address1'
    ADDRESS2 ='address2'
    CITY = 'city'
    STATE = 'id_state'
    POST_CODE = 'postcode'
    COUNTRY = 'id_country'
    OTHER = 'other'
    HOME_PHONE = 'phone'
    MOBILE_PHONE ='phone_mobile'
    ALIAS_ADDRESS = 'alias'
    REGISTER = 'submitAccount'
    MY_ACCOUNT = 'account'

    def set_email(self, email_id):
        self._driver.find_element_by_id(SignUp.EMAIL_ID).send_keys(email_id)

    def reg_button(self):
        return self._driver.find_element_by_id(SignUp.SUBMIT_CREATE).is_displayed()

    def signup(self):
        self._driver.find_element_by_id(SignUp.SUBMIT_CREATE).click()

    def set_title(self):
        self._driver.find_element_by_id(SignUp.TITLE).click()

    def set_firstName(self, f_name: str):
        self._driver.find_element_by_id(SignUp.FIRST_NAME).send_keys(f_name)

    def set_lastName(self, l_name: str):
        self._driver.find_element_by_id(SignUp.LAST_NAME).send_keys(l_name)

    def set_passWord(self, password):
        self._driver.find_element_by_id(SignUp.PASSWORD).send_keys(password)

    def set_dOB(self, date):
        choose1 = Select(self._driver.find_element_by_id(SignUp.DAY))
        choose1.select_by_value(date)

    def set_mOB(self, month):
        choose1 = Select(self._driver.find_element_by_id(SignUp.MONTH))
        choose1.select_by_value(month)

    def set_yOB(self, year):
        choose1 = Select(self._driver.find_element_by_id(SignUp.YEAR))
        choose1.select_by_value(year)

    def set_newsLetter(self):
        self._driver.find_element_by_id(SignUp.NEWS_LETTER).click()

    def set_splOffers(self):
        self._driver.find_element_by_id(SignUp.OFFERS).click()

    def set_addFN(self, add_f_name: str):
        self._driver.find_element_by_id(SignUp.ADDRESS_FN).send_keys(add_f_name)

    def set_addLN(self, add_l_name: str):
        self._driver.find_element_by_id(SignUp.ADDRESS_LN).send_keys(add_l_name)

    def set_company(self, company):
        self._driver.find_element_by_id(SignUp.COMPANY).send_keys(company)

    def set_address1(self, address1):
        self._driver.find_element_by_id(SignUp.ADDRESS1).send_keys(address1)

    def set_address2(self, address2):
        self._driver.find_element_by_id(SignUp.ADDRESS2).send_keys(address2)

    def set_city(self, city: str):
        self._driver.find_element_by_id(SignUp.CITY).send_keys(city)

    def set_state(self, state):
        choose1 = Select(self._driver.find_element_by_id(SignUp.STATE))
        choose1.select_by_value(state)

    def set_zipCode(self, zip):
        self._driver.find_element_by_id(SignUp.POST_CODE).send_keys(zip)

    def set_country(self, country):
        choose1 = Select(self._driver.find_element_by_id(SignUp.COUNTRY))
        choose1.select_by_value(country)

    def set_additional_info(self, other):
        self._driver.find_element_by_id(SignUp.OTHER).send_keys(other)

    def set_homePhone(self, phone: int):
        self._driver.find_element_by_id(SignUp.HOME_PHONE).send_keys(phone)

    def set_mobilePhone(self, phone: int):
        self._driver.find_element_by_id(SignUp.MOBILE_PHONE).send_keys(phone)

    def set_aliasAddress(self, alias: str):
        self._driver.find_element_by_id(SignUp.ALIAS_ADDRESS).send_keys(alias)

    def register(self):
        self._driver.find_element_by_id(SignUp.REGISTER).click()

    def result(self):
        return self._driver.find_element_by_class_name(SignUp.MY_ACCOUNT).is_displayed()











