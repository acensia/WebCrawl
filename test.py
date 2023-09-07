from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get("https://www.musinsa.com/app/goods/3055600/0")
# Check page content before alert
page_content_before = driver.page_source
if not body_content.strip():
    print("Here")
    driver.quit()
    exit()

driver.find_elements(By.XPATH, '//div[class@="hi"]')

driver.quit()