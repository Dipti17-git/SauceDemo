from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# POSITIVE TEST - Valid Login
def test_valid_login(driver):
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Assert successful login
    assert "inventory.html" in driver.current_url, "Login should succeed with valid credentials"
    print("✅ Positive test passed: Valid login successful")

    # Logout for next test
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()

# NEGATIVE TEST - Invalid Credentials
def test_invalid_login(driver):
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    # Assert error message appears
    error_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )
    assert error_message.is_displayed(), "Error message should appear for invalid credentials"
    assert "Username and password do not match" in error_message.text, "Incorrect error message"
    assert "inventory.html" not in driver.current_url, "Should not redirect on failed login"
    print("✅ Negative test passed: Invalid login properly rejected")