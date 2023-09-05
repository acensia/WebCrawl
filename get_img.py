from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import json


def get_imgs(driver, save_path):
    image_element = driver.find_elements(By.XPATH, '//div[@class="codimap-cont"]/img')

    image_url = image_element[0].get_attribute('src')
    response = requests.get(image_url)
    with open(f'{save_path}/set_image.jpg', 'wb') as file:
        file.write(response.content)
    # Close the driver

    image_singles = driver.find_elements(By.CSS_SELECTOR, '.swiper-slide.style_contents_size')
    
    img_single = driver.find_elements(By.XPATH, '//a[@class="styling_img"]/img')
    brand_single = driver.find_elements(By.XPATH, '//a[@class="brand"]')
    brand_items = driver.find_elements(By.XPATH, '//a[@class="brand_item"]')
    price_items = driver.find_elements(By.XPATH, '//div[@class="price"]')
    
    anno = {}
    anno["set_name"] = driver.find_element(By.XPATH, '//div[@class="styling_content codimap-contents"]/h2').text
    items = []
    
    for i, s in enumerate(img_single):
        img_url = s.get_attribute('src')
        res = requests.get(img_url)
        with open(f"{save_path}/img{i}.jpg", 'wb') as f:
            f.write(res.content)
        
        item = {}
        item["brand"] = brand_single[i].text
        item["item"] = brand_items[i].text
        item["curr_price"] = price_items[i].text
        items.append(item)
    anno["items"] = items
    with open(f"{save_path}/anno.json", 'w', encoding='utf-8') as f:
        json.dump(anno, f, indent=4, ensure_ascii=False)
        
        