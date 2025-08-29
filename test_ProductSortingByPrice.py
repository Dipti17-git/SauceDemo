from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

def test_sorting_price_desc():
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Select "Price (high to low)"
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (high to low)")

    # Collect prices
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_values = [float(price.text.replace("$", "")) for price in prices]

    # Assert sorted descending
    assert price_values == sorted(price_values, reverse=True), "Prices are not sorted high to low"
    print("✅ Price sorting (high to low) works correctly.")

if __name__ == "__main__":
    test_sorting_price_desc()
    driver.quit()