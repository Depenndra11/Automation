import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():

    options = Options()

    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    return driver