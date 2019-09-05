from src.PageObject.home_page import HomePage
from src.PageObject.search_page import SearchPage
from TestBase.test_template import TestTemplate

class TestSearchPage(TestTemplate):

    def test_result_found(self):
        home_page = HomePage(self.driver)
        home_page.set_search_query('dress')
        home_page.check_search()
        home_page.search()
        result = SearchPage(self.driver)
        assert result.check_page_source('dress')

