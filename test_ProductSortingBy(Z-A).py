from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

def test_sorting_name_desc():
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Select "Name (Z to A)"
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Name (Z to A)")

    # Collect product names
    item_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [item.text for item in item_names]
    print(product_names)

    # Prepare expected sorted lists
    sorted_names = sorted(product_names)
    sorted_names_desc = sorted(product_names, reverse=True)

    # Assert Z → A sorting is correct
    assert product_names == sorted_names_desc, "Products are not sorted Z to A"
    print("✅ Name sorting (Z to A) works correctly!")

if __name__ == "__main__":
    test_sorting_name_desc()
    driver.quit()