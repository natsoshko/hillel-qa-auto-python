from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    about_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "// button[text() = 'About']"))
    )

    about_button.click()
    print("'About' button is found and clicked")

finally:
    driver.quit()