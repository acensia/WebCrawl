from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests as rq
import os
from jungo_single import get_imgs
import re
from urllib.parse import quote
import json



def search(korean):
    os.makedirs("./jungo", exist_ok=True)

    driver = webdriver.Chrome()

    url_encoded_string = quote(korean, encoding='UTF-8')

    print(url_encoded_string)

    
    total_sets = 0
    page = 1
    limit = 200
    while total_sets < limit:
        items = []
        # get into page numbered as "page" value
        driver.get(f"https://web.joongna.com/search/{url_encoded_string}?page={page}")
        
        # get all of thumnail elements in catalog
        image_thumbnails = driver.find_elements(By.XPATH, '//a[@class="group box-border overflow-hidden flex rounded-md cursor-pointer pe-0 pb-2 lg:pb-3 flex-col items-start transition duration-200 ease-in-out transform hover:-translate-y-1 md:hover:-translate-y-1.5 hover:shadow-product bg-white"]')
        url_list = []
        for th in image_thumbnails:
            url_list.append(th.get_attribute('href'))
        for u in url_list:
            driver.get(u) # get into the page of each set clicking the thumbnail
            time.sleep(0.5)
            single = get_imgs(driver) # call module
            time.sleep(0.5)
            items.append(single)
            total_sets += 1
            if total_sets == limit:
                break
        j = {}
        j["list"] = items
        with open(f"./jungo/list_{page}.json", 'w', encoding='utf-8') as f:
            json.dump(j, f, ensure_ascii=False)
        page += 1

    


    driver.quit()

if __name__ == "__main__":
    search("셔츠")