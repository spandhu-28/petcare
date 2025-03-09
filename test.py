from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("C:/Users/HP/OneDrive/Desktop/PetCare-main/PetCare-main/index.html")

WebDriverWait(driver, 100).until(EC.title_contains("PetCare-main"))

assert "PetCare-main" in driver.title

driver.quit()