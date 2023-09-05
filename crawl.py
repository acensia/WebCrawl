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
    print(len(image_singles))
    for i, s in enumerate(image_singles):
        img = s.find_elements(By.XPATH, '//a[@class="styling_img"]/img')
        print(img)
        img_url = img[0].get_attribute('src')
        res = requests.get(img_url)
        with open(f"{save_path}/img{i}.jpg", 'wb') as f:
            f.write(res.content)