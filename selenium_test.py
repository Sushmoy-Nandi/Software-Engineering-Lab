import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Set up the browser
# We use options to keep the window open and maximized
opt = Options()
opt.add_argument("--start-maximized")
# This line just hides the "Chrome is being controlled..." bar
# opt.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=opt)

# Simple function to make clicking easier
# It waits a bit before clicking so the script doesn't crash
def safe_click(id_value):
    time.sleep(1) # small wait to be safe
    driver.find_element(By.ID, id_value).click()

# Function to type text safely (fix for the React bug)
def type_text(id_value, text):
    time.sleep(0.5)
    box = driver.find_element(By.ID, id_value)
    box.click()
    # clear the field first using keys
    box.send_keys(Keys.CONTROL + "a")
    box.send_keys(Keys.BACKSPACE)
    box.send_keys(text)

# --- Start of the Test ---

# 1. Open website
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# 2. Login
type_text("user-name", "standard_user")
type_text("password", "secret_sauce")
safe_click("login-button")
print("Login successful")
time.sleep(2)

# 3. Add item to cart
safe_click("add-to-cart-sauce-labs-backpack")
print("Added to cart")
time.sleep(2)

# 4. Remove item (testing the button)
safe_click("remove-sauce-labs-backpack")
print("Removed from cart")
time.sleep(2)

# 5. Add it back again
safe_click("add-to-cart-sauce-labs-backpack")
print("Added again")
time.sleep(2)

# 6. Go to Cart page
# (We use class name here because there is no ID for the cart icon)
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
print("Cart page opened")
time.sleep(2)

# 7. Click Checkout
safe_click("checkout")
time.sleep(2)

# 8. Fill in details
type_text("first-name", "Test")
type_text("last-name", "Student")
type_text("postal-code", "1234")
safe_click("continue")
print("Checkout info filled")
time.sleep(2)

# 9. Finish the order
safe_click("finish")
print("Order completed")
time.sleep(2)

# 10. Logout process
safe_click("react-burger-menu-btn")
time.sleep(1) # wait for menu animation
safe_click("logout_sidebar_link")
print("Logout successful")
time.sleep(2)

# Close everything
driver.quit()