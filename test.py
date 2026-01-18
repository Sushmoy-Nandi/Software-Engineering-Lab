import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup Browser
opt = Options()
opt.add_argument("--start-maximized")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=opt)


def safe_click(id_value):
    time.sleep(1)
    driver.find_element(By.ID, id_value).click()


def type_text(id_value, text):
    driver.find_element(By.ID, id_value).send_keys(text)


try:
    # --- Step 1: Browse the website ---
    driver.get("https://www.saucedemo.com/")
    print("1. Browse the website")
    time.sleep(2)

    # --- Step 2: Perform Login with Valid Credentials ---
    type_text("user-name", "standard_user")
    type_text("password", "secret_sauce")
    safe_click("login-button")
    print("2. Login Successful")
    time.sleep(2)

    # --- Step 3: Add multiple items to the cart ---
    # We add TWO items to satisfy "multiple"
    safe_click("add-to-cart-sauce-labs-backpack")
    safe_click("add-to-cart-sauce-labs-bike-light")
    print("3. Multiple items added to cart")
    time.sleep(2)

    # --- Step 4: Go to Cart and Remove item ---
    # Click Cart Icon (Class name used as it has no ID)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # Remove one item (The Backpack)
    safe_click("remove-sauce-labs-backpack")
    print("4. Went to Cart and removed an item")
    time.sleep(2)

    # --- Step 5: Click 'Continue Shopping' and Logout ---
    safe_click("continue-shopping")
    print("5. Clicked Continue Shopping (Back to Home)")
    time.sleep(2)

    # Perform Logout
    safe_click("react-burger-menu-btn")
    time.sleep(1)  # Wait for menu animation
    safe_click("logout_sidebar_link")
    print("5. Logout Performed")
    time.sleep(2)

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()