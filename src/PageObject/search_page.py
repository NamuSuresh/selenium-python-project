from src.PageObject.base_page import BasePage


class SearchPage(BasePage):
    PRODUCT_LISTING = 'page-heading  product-listing'
    PAGE_HEADING = 'lighter'
    RESULT_COUNT = 'heading-counter'


    def productlist(self):
        return self._driver.find_element_by_class_name(SearchPage.PRODUCT_LISTING).text


    def lighter_search_heading(self):
        return self._driver.find_element_by_xpath(SearchPage.PAGE_HEADING).text

    def result_count(self):
        return self._driver.find_element_by_class_name(SearchPage.RESULT_COUNT).text

    def check_page_source(self, value):
        return value in self._driver.page_source