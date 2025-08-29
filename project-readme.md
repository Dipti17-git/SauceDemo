# SauceDemo Test Automation Project

A Selenium-based test automation suite for the SauceDemo e-commerce application, built with Python and pytest framework.

## 🚀 How to Install & Run

### Prerequisites
- Python 3.8+
- Chrome Browser (139.0.7258.154)


1. Setup done for Pytest in local machine [Taken help from Perplexity]

2. **Install dependencies**
```bash
pip install selenium pytest webdriver-manager pytest-html allure-pytest
```

3. **Run tests**
```bash
# Run all tests
pytest -v

# Generate HTML report
pytest -v --html=report.html --self-contained-html

# Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

### Running Specific Tests
```bash
# Login tests only
pytest test_login.py -v

# Sorting tests only
pytest test_sorting.py -v

# Run with custom markers
pytest -m smoke -v
```

## 📋 What has been Covered

### 1. **Core Test Scenarios**
- **Login Functionality**
  - Valid login with standard user credentials
  - Invalid login with wrong username/password
  - Empty field validation (username/password required)
  - Locked user account handling
  - Logout functionality

- **Product Sorting**
  - Name sorting (A to Z / Z to A)
  - Price sorting (Low to High / High to Low)
  - Default sorting validation
  - Sort dropdown options verification

- **Shopping Cart & Checkout**
  - Add multiple products to cart
  - Cart item count validation
  - Checkout process with form validation
  - Order total calculation verification
  - End-to-end purchase flow

### 2. **Test Architecture & Best Practices**
- **pytest Framework Implementation**
  - Proper test class structure with fixtures
  - Setup and teardown for WebDriver management
  - Parametrized tests for data-driven testing
  - Custom markers for test categorization

- **Page Object Model Concepts**
  - Separation of test logic and page interactions
  - Reusable element locators
  - Clean test code organization

- **WebDriver Management**
  - Automatic ChromeDriver version management using webdriver-manager
  - Browser options optimization for testing
  - Cross-browser compatibility setup

### 3. **Reporting & Documentation**
- **HTML Test Reports**
  - pytest-html integration for detailed test results
  - Screenshot capture on test failures
  - Custom test descriptions and assertions

- **Allure Reports**
  - Professional test reporting with step-by-step execution
  - Test categorization with epics, features, and stories
  - Screenshot attachments and test metadata
  - Historical test data tracking

### 4. **Stability & Anti-Flakiness Techniques**
- Explicit waits using WebDriverWait and Expected Conditions
- Robust element locators using stable selectors (ID, name attributes)
- Retry mechanisms for intermittent failures
- Proper test isolation with independent WebDriver instances
- Chrome popup handling (password manager, notifications)

### 5. **Advanced Selenium Concepts**
- Select dropdown handling for sorting functionality
- List comprehensions for data extraction and validation
- Dynamic element location strategies
- JavaScript execution for complex interactions
- File upload automation techniques

## 🛠️ What You'd Add With More Time

### 1. **Enhanced Test Coverage**
- **User Management Tests**
  - Different user types (problem_user, performance_glitch_user)
  - User session management
  - Password reset functionality

- **Advanced E-commerce Features**
  - Product filtering and search
  - Wishlist functionality
  - Product comparison features
  - Inventory management validation

- **Cross-Browser Testing**
  - Firefox, Safari, Edge compatibility
  - Mobile responsive testing
  - Different screen resolution testing

### 2. **Advanced Framework Features**
- **API Testing Integration**
  - Backend API validation
  - API and UI test data consistency
  - Performance testing with API calls

- **Database Validation**
  - Order data persistence verification
  - User data integrity checks
  - Inventory level validation

- **Performance Testing**
  - Page load time monitoring
  - Response time validation
  - Memory usage tracking

### 3. **CI/CD Pipeline Enhancement**
- **Automated Test Execution**
  - GitHub Actions / Jenkins integration
  - Scheduled test runs
  - Pull request validation

- **Docker Containerization**
  - Containerized test environment
  - Selenium Grid setup
  - Scalable test execution

- **Advanced Reporting**
  - Test trend analysis
  - Failure pattern recognition
  - Integration with monitoring tools

### 4. **Code Quality & Maintenance**
- **Advanced Page Object Model**
  - Component-based page objects
  - Page factory implementation
  - Dynamic page object generation

- **Test Data Management**
  - External test data sources (JSON, CSV, databases)
  - Test data cleanup and reset mechanisms
  - Environment-specific test configurations

## 🔍 Assumptions You Made

### 1. **Application Assumptions**
- **SauceDemo Environment**: Assumed the demo site remains stable and accessible at https://www.saucedemo.com/
- **User Credentials**: Used publicly available demo credentials (standard_user/secret_sauce)
- **Product Inventory**: Assumed product list and prices remain relatively stable for sorting validation
- **Browser Compatibility**: Primarily focused on Chrome browser for consistent testing

### 2. **Testing Environment**
- **Local Execution**: Tests designed to run on local development machines
- **Chrome Browser**: Assumed Chrome is the primary browser for test execution
- **Python Environment**: Assumed Python 3.8+ availability with pip package manager
- **Network Connectivity**: Assumed stable internet connection for external site access

### 3. **Test Data & Scope**
- **Limited User Types**: Focused on standard_user for most scenarios
- **Static Test Data**: Used hardcoded test data for simplicity and reliability
- **English Language**: Assumed English language interface and content
- **Desktop Testing**: Primarily focused on desktop browser testing

### 4. **Technical Assumptions**
- **Port Availability**: Assumed standard ports (9222-9230) available for WebDriver communication
- **File System Access**: Assumed write permissions for screenshot and report generation
- **Chrome Driver**: Relied on webdriver-manager for automatic driver management

## 🛡️ How You Kept Tests Stable

### 1. **Robust Element Location**
```python
# Used stable, unique locators
driver.find_element(By.ID, "user-name")  # ID is most stable
driver.find_element(By.NAME, "password")  # Name attribute as fallback

# Avoided fragile CSS selectors
# Bad: driver.find_element(By.CSS_SELECTOR, "div > div > input:nth-child(2)")
# Good: driver.find_element(By.ID, "login-button")
```

### 2. **Explicit Wait Strategies**
```python
# Implemented proper wait conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Wait for element to be clickable
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)

# Wait for URL change after actions
WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
```

### 3. **Chrome Configuration Optimization**
```python
chrome_options = Options()
# Disable password manager popups
chrome_options.add_argument("--disable-password-manager")
chrome_options.add_argument("--disable-save-password-bubble")
chrome_options.add_argument("--disable-notifications")

# Performance optimizations
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

# Prevent automation detection
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
```

### 4. **Error Handling & Retry Mechanisms**
```python
# Implemented retry logic for WebDriver creation
for attempt in range(3):
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        break
    except Exception as e:
        if attempt < 2:
            time.sleep(2)
        else:
            raise e
```




### 5. **Assertion Best Practices**
```python
# Clear, specific assertions with meaningful error messages
assert "inventory.html" in driver.current_url, "Login should redirect to inventory page"
assert product_names == sorted(product_names), f"Products not sorted A-Z. Got: {product_names}"

# Verify element presence before interaction
assert driver.find_element(By.ID, "shopping_cart_link").is_displayed(), "Cart link should be visible"
```

### 6. **Screenshot Capture for Debugging**
```python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.failed and hasattr(item, 'funcargs'):
        if 'driver' in item.funcargs:
            driver = item.funcargs['driver']
            # Capture screenshot on failure
            driver.save_screenshot(f"failure_{item.name}.png")
```

---

## 📊 Test Execution Summary

- **Total Test Categories**: 5 (Login, Sorting, Cart/Checkout, Navigation, File Upload)
- **Stability Techniques**: 8 implemented anti-flakiness measures
- **Reporting Options**: 2 (HTML, Allure) with screenshot integration
- **Browser Support**: Chrome optimized with cross-browser capability
- **Framework**: pytest with fixtures, parametrization, and markers

**Success Rate Target**: 95%+ test stability through implemented anti-flakiness techniques.