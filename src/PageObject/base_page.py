class BasePage(object):

    def __init__(self, driver):
        self._driver = driver
        driver.maximize_window()

