from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests as rq
import os
from crawl import get_imgs

# Initialize the driver
driver = webdriver.Chrome()

total_sets = 0
page = 1

os.makedirs("./casual", exist_ok=True)

while total_sets < 3:
    driver.get(f"https://www.musinsa.com/app/codimap/lists?style_type=casual&tag_no=&brand=&display_cnt=60&list_kind=big&sort=date&page={page}")
    
    
    image_thumbnails = driver.find_elements(By.XPATH, '//div[@class="style-list-thumbnail"]/img')
    for th in image_thumbnails:
        os.makedirs(f"./casual/{total_sets}", exist_ok=True)
        th.click()
        time.sleep(0.5)
        get_imgs(driver, f"./casual/{total_sets}")
        
        driver.back()
        time.sleep(0.5)
        total_sets += 1
    
    page += 1 
    
driver.quit()