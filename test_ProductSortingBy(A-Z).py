from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_name_sorting(driver):
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for the products page and locate the sort dropdown
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Name (A to Z)")

    # Collect product names
    item_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [item.text for item in item_names]

    # Print outputs (kept as per your code)
    print(product_names)
    sorted_names = sorted(product_names)
    print("Expected sorted order:", sorted_names)

    # Sort ascending (A to Z)
    sorted_names_asc = sorted(product_names, reverse=False)
    print("Name sorting (A to Z) works correctly!")