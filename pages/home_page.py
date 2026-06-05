from selenium.webdriver.common.by import By

class HomePage:

    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        self.driver = driver

    def open_amazon(self):
        self.driver.get("https://www.amazon.in")

    def search_product(self, product):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(product)
        self.driver.find_element(*self.SEARCH_BUTTON).click()