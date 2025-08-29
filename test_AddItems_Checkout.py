from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import tempfile
# setup Chrome options

def make_driver():
    chrome_options = Options()

    # 1) Turn off Chrome’s password manager & leak detection
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,  # important
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # 2) Disable features that can surface the dialog
    chrome_options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--incognito")  # password manager UI is off in incognito

    # 3) Use a fresh, empty profile so old settings don’t override ours
    tmp_profile = tempfile.mkdtemp(prefix="chrome-profile-")
    chrome_options.add_argument(f"--user-data-dir={tmp_profile}")

    # (optional) hide automation banner/log spam
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    return webdriver.Chrome(options=chrome_options)

# --- usage ---
driver = make_driver()
driver.get("https://www.saucedemo.com/")


def test_checkout_flow():
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add first product (Sauce Labs Backpack - $29.99)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Add second product (Sauce Labs Bolt T-Shirt - $15.99)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # Go to shopping cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verify 2 items in cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 2, f"Expected 2 items in cart, found {len(cart_items)}"

    # Get individual prices from cart
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_values = [float(price.text.replace("$", "")) for price in prices]
    expected_subtotal = sum(price_values)

    print(f"Individual prices: {price_values}")
    print(f"Expected subtotal: ${expected_subtotal}")

    # Proceed to checkout
    driver.find_element(By.ID, "checkout").click()

    # Fill checkout information
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    # Get subtotal, tax, and total from checkout overview
    subtotal_element = driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
    tax_element = driver.find_element(By.CLASS_NAME, "summary_tax_label")
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")

    # Extract numeric values
    subtotal = float(subtotal_element.text.replace("Item total: $", ""))
    tax = float(tax_element.text.replace("Tax: $", ""))
    total = float(total_element.text.replace("Total: $", ""))

    print(f"Checkout subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Final total: ${total}")

    # Assert subtotal matches expected
    assert subtotal == expected_subtotal, f"Subtotal mismatch: expected ${expected_subtotal}, got ${subtotal}"

    # Assert total equals subtotal + tax
    expected_total = subtotal + tax
    assert total == expected_total, f"Total mismatch: expected ${expected_total}, got ${total}"

    print("✅ All assertions passed! Cart total calculation is correct.")

    # Complete the order (optional)
    driver.find_element(By.ID, "finish").click()

    # Verify order completion
    success_message = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "Thank you for your order!" in success_message.text

    print("✅ Order completed successfully!")

if __name__ == "__main__":
    test_checkout_flow()
    driver.quit()