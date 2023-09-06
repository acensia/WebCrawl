from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import json


def get_imgs(driver, save_path):
    # get the image of the set
    image_element = driver.find_elements(By.XPATH, '//div[@class="codimap-cont"]/img')
    image_url = image_element[0].get_attribute('src')
    response = requests.get(image_url)
    with open(f'{save_path}/set_image.jpg', 'wb') as file:
        file.write(response.content)

    img_single = driver.find_elements(By.XPATH, '//a[@class="styling_img"]/img') # get the images of each cloth constructing the set
    img_links = driver.find_elements(By.XPATH, '//a[@class="styling_img"]') # get the images of each cloth constructing the set
    brand_single = driver.find_elements(By.XPATH, '//a[@class="brand"]') # get the brand of each cloth
    brand_items = driver.find_elements(By.XPATH, '//a[@class="brand_item"]') # get the name of each cloth
    price_items = driver.find_elements(By.XPATH, '//div[@class="price"]') # get the price of each cloth (not completed)
    
    anno = {}
    anno["set_name"] = driver.find_element(By.XPATH, '//div[@class="styling_content codimap-contents"]/h2').text # get the name of the set
    items = []
    
    for i, s in enumerate(img_single):
        img_url = s.get_attribute('src') # single image
        res = requests.get(img_url)
        with open(f"{save_path}/img{i}.jpg", 'wb') as f:
            f.write(res.content)
        
        item = {} # annotation info
        item["brand"] = brand_single[i].text
        item["item"] = brand_items[i].text
        item["curr_price"] = price_items[i].text
        item["link"] = img_links[i].get_attribute('href')
    
        items.append(item)
        
        
    anno["items"] = items
    with open(f"{save_path}/anno.json", 'w', encoding='utf-8') as f:
        json.dump(anno, f, indent=4, ensure_ascii=False)
        
        