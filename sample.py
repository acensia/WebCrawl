from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Initialize the driver
driver = webdriver.Chrome()

# Open Google
driver.get('https://www.google.com')

# Find the search box
search_box = driver.find_element(By.NAME, 'q')

# Type 'Selenium' and hit Enter
search_box.send_keys('Selenium')
search_box.send_keys(Keys.RETURN)

# Wait until the search results are loaded
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )
except TimeoutException:
    print("Timed out waiting for the search results to load.")
    driver.quit()

# Get the titles of the first 3 search results
# titles = driver.find_elements(By.XPATH, '//div[@class="tF2Cxc"]/div[1]/a/h3')
titles = driver.find_elements(By.XPATH, '//h3[@class="LC20lb MBeuO DKV0Md"]')
print(titles[:3])
for i, title in enumerate(titles[:3]):
    print(f"Result {i + 1}: {title.text}")

# Close the driver
driver.quit()
