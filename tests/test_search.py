from pages.home_page import HomePage

def test_search_product(driver):

    home = HomePage(driver)

    home.open_amazon()

    home.search_product("iPhone")

    assert "iphone" in driver.title.lower()