from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Authorisation
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    # Step 1: Click on button "Guest log in"
    user_menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.header-link.-guest"))
    )
    user_menu_button.click()

    # Step 2: Find element 'My Profile' button => Garage
    profile_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "userNavDropdown"))
    )
    profile_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "nav.user-nav_menu.dropdown-menu.show")
        )
    )

    garage_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "nav a.dropdown-item.btn.user-nav_link[href*='garage']")
        )
    )
    if "panel/garage" not in driver.current_url:
        garage_link.click()
    else:
        print("Garage is disabled")

finally:
    driver.quit()