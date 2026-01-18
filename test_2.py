import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ================= SETUP =================
# Step 1: Browse the website (OrangeHRM)
URL = "https://opensource-demo.orangehrmlive.com/"

opt = Options()
opt.add_argument("--start-maximized")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=opt)
wait = WebDriverWait(driver, 10)


# ================= FUNCTIONS =================
def click_xpath(xpath):
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


def type_name(name, text):
    # OrangeHRM uses 'name' attributes, not IDs
    el = wait.until(EC.presence_of_element_located((By.NAME, name)))
    el.send_keys(text)


try:
    driver.get(URL)
    # OrangeHRM takes a moment to load the login form
    time.sleep(3)

    # --- Step 2: Perform Login ---
    # Default Creds for OrangeHRM: Admin / admin123
    type_name("username", "Admin")
    type_name("password", "admin123")
    click_xpath("//button[@type='submit']")

    # Wait for dashboard to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar-header-title")))
    print("2. Login Successful")
    time.sleep(2)

    # --- Step 3 & 4: Add/Remove Items (IMPOSSIBLE ON THIS SITE) ---
    print("\n--- NOTE TO EXAMINER ---")
    print("Steps 3 (Add to Cart) and 4 (Remove from Cart) cannot be performed.")
    print("Reason: OrangeHRM is an HR website and does not have a Shopping Cart.")
    print("Skipping to Step 5...")
    print("------------------------\n")
    time.sleep(3)

    # --- Step 5: Logout ---
    # Logout is hidden in the user dropdown menu on OrangeHRM
    click_xpath("//span[@class='oxd-userdropdown-tab']")
    time.sleep(1)  # Wait for dropdown animation
    click_xpath("//a[text()='Logout']")

    print("5. Logout Performed")
    time.sleep(2)

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    driver.quit()