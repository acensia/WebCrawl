from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests as rq
import os
from get_img import get_imgs


styles = ["casual", "formal", "sports", "street", "gorpcore", "dandy"]
def crawl_style(style, base_path):
    
    # Initialize the driver
    driver = webdriver.Chrome()
    
    os.makedirs(f"{base_path}/{style}", exist_ok=True)
    os.makedirs(f"{base_path}/{style}/male", exist_ok=True)
    os.makedirs(f"{base_path}/{style}/female", exist_ok=True)
    page = 1
    total_sets = 0
    while total_sets < 200:
        driver.get(f"https://www.musinsa.com/app/codimap/lists?style_type={style}&tag_no=&brand=&display_cnt=60&list_kind=big&sort=date&page={page}")
        btns = driver.find_elements(By.XPATH, '//div[@class="sc-pvystx-0 iRAZYo"]/button')
        driver.execute_script("arguments[0].click();", btns[1])
        
        image_thumbnails = driver.find_elements(By.XPATH, '//div[@class="style-list-thumbnail"]/img')
        for th in image_thumbnails:
            print(f"{style} : {total_sets}")
            os.makedirs(f"{base_path}/{style}/male/{total_sets}", exist_ok=True)
            driver.execute_script("arguments[0].click();", th)
            time.sleep(0.3)
            get_imgs(driver, f"{base_path}/{style}/male/{total_sets}")
            
            driver.back()
            time.sleep(0.3)
            total_sets += 1
            if total_sets == 200:
                break
            
        page += 1

    page = 1
    total_sets = 0        
    
    while total_sets < 200:
        driver.get(f"https://www.musinsa.com/app/codimap/lists?style_type={style}&tag_no=&brand=&display_cnt=60&list_kind=big&sort=date&page={page}")
        btns = driver.find_elements(By.XPATH, '//div[@class="sc-pvystx-0 iRAZYo"]/button')
        driver.execute_script("arguments[0].click();", btns[2])
        
        image_thumbnails = driver.find_elements(By.XPATH, '//div[@class="style-list-thumbnail"]/img')
        for th in image_thumbnails:
            print(f"{style} : {total_sets}")
            os.makedirs(f"./shown/{style}/female/{total_sets}", exist_ok=True)
            driver.execute_script("arguments[0].click();", th)
            time.sleep(0.3)
            get_imgs(driver, f"./shown/{style}/female/{total_sets}")
            
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
        crawl_style(st, base_path)
        print(f"{st} completed")