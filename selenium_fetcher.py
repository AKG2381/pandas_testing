import os
from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions


chromdriver_path = os.environ.get("CHROMEDRIVER_PATH",'usr/bin/chromedriver')
print(chromdriver_path)


def conect_to_browser():
    """
    Connect to the chrome browser in headless mode.

    Returns:
        selenium.webdriver.chrome.webdriver.WebDriver: The chrome driver
    """
    # Set the options for the chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run the browser in headless mode
    options.add_argument('no-sandbox')  # Disable sandboxing for heroku
    # Create the chrome driver
    driver = webdriver.Chrome(executable_path=chromdriver_path)
    return driver

def fetch_data(url):
    driver = conect_to_browser()
    driver.get(url)
    page_source = driver.page_source
    return page_source