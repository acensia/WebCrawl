from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import json


def get_imgs(driver):
    item = {}
    cate = driver.find_elements(By.XPATH, '//ol[@class="flex items-center w-full"]/li/a')
    item["categories"] = cate[0].text
    img = driver.find_elements(By.XPATH, '//img[@class="object-cover w-full h-full rounded-lg top-1/2 left-1/2"]')
    img_url = img[0].get_attribute('src')
    item["url"] = img_url

    return item