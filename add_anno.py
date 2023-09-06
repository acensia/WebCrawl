import os, glob, json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# base_path, gender, style, number
set_dirs = glob.glob(os.path.join("./added", "*", "*", "*"))

driver = webdriver.Chrome()

for folder in set_dirs:
    with open(f"{folder}/anno.json", 'r', encoding='utf-8') as j:
        anno_d = json.load(j)
    for i_d in anno_d["items"]:
        single_url = i_d["link"]
        driver.get(single_url)
        texts = driver.find_elements(By.XPATH, '//p[@class="item_categories"]/a')
        i_d["type"] = texts[0].text
        i_d["label"] = texts[1].text
        
    with open(f"{folder}/anno_added.json", 'w', encoding='utf-8') as j:
        json.dump(anno_d, j, indent=4, ensure_ascii=False)
