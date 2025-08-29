import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Chrome browser setup
    options = Options()
    options.add_argument("--headless=new")      # run in headless mode (no browser window).
                                               # remove this line if you want to SEE the browser.
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)                  # waits up to 10s for elements
    driver.get("https://www.saucedemo.com/")    # starting URL
    yield driver                                # this gives driver to your test
    driver.quit()