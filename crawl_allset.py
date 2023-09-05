from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests as rq
import os
from get_img import get_imgs
import re

# target styles
styles = ["casual", "formal", "sports", "street", "gorpcore", "dandy"]

# gender value 
def crawl_style(style, base_path, gender):
    
    # Initialize the driver
    driver = webdriver.Chrome()
    
    os.makedirs(f"{base_path}/{style}", exist_ok=True)
    os.makedirs(f"{base_path}/{style}/{gender}", exist_ok=True)
    
    page = 1
    total_sets = 0
    limit = 200
    if gender == "male":
        idx = 1
    else :
        idx = 2
    
    # check limitation of the number of cloth sets for male
    # 1. get into male catalog
    driver.get(f"https://www.musinsa.com/app/codimap/lists?style_type={style}&tag_no=&brand=&display_cnt=60&list_kind=big&sort=date&page={page}")
    btns = driver.find_elements(By.XPATH, '//div[@class="sc-pvystx-0 iRAZYo"]/button')
    driver.execute_script("arguments[0].click();", btns[idx])
    # 2. get total nums of sets
    cnt = driver.find_element(By.XPATH, '//span[@class="counter"]')
    num_text = cnt.text
    match = re.search(r'(\d{1,3}(?:,\d{3})*)', num_text)
    num_str = match.group(1)
    num = int(num_str.replace(',', ''))
    
    if num < limit:
        print("The num of sets is less than limit")
        limit = num
        
            
    while total_sets < limit:
        # get into page numbered as "page" value
        driver.get(f"https://www.musinsa.com/app/codimap/lists?style_type={style}&tag_no=&brand=&display_cnt=60&list_kind=big&sort=date&page={page}")
        btns = driver.find_elements(By.XPATH, '//div[@class="sc-pvystx-0 iRAZYo"]/button')
        driver.execute_script("arguments[0].click();", btns[idx])
    
        # get all of thumnail elements in catalog
        image_thumbnails = driver.find_elements(By.XPATH, '//div[@class="style-list-thumbnail"]/img')
        for th in image_thumbnails:
            print(f"{style} : {total_sets}") # just for monitoring
            os.makedirs(f"{base_path}/{style}/{gender}/{total_sets}", exist_ok=True)
            driver.execute_script("arguments[0].click();", th) # get into the page of each set clicking the thumbnail
            time.sleep(0.3)
            get_imgs(driver, f"{base_path}/{style}/{gender}/{total_sets}") # call module
            driver.back()
            time.sleep(0.3)
            total_sets += 1
            if total_sets == 200:
                break
            
        page += 1
        
    driver.quit()
    
if __name__ == "__main__":
    
    base_path = "./gendered"
    os.makedirs(base_path, exist_ok=True)
    
    for st in styles:
        crawl_style(st, base_path, "male")
        print(f"{st} completed")