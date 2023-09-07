import os, glob, json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# base_path, gender, style, number
set_dirs = glob.glob(os.path.join("./added", "male", "*", "*"))

driver = webdriver.Chrome()

for folder in set_dirs:
    with open(f"{folder}/anno.json", 'r', encoding='utf-8') as j:
        anno_d = json.load(j)
    fold = folder.split("\\")
    # print(fold)
    print(f"{fold[1]}, {fold[2]} : {fold[3]}")
    # if fold[1] == 'male' and fold[2] == 'casual' and int(fold[3][0]) < 6:
    #     continue
    for i_d in anno_d["items"]:
        single_url = i_d["link"]
        driver.get(single_url)
        time.sleep(0.4)
        texts = driver.find_elements(By.XPATH, '//p[@class="item_categories"]/a')
        i_d["type"] = texts[0].text
        if len(texts) < 2:
            continue
        i_d["label"] = texts[1].text
        
    with open(f"{folder}/anno_added.json", 'w', encoding='utf-8') as j:
        json.dump(anno_d, j, indent=4, ensure_ascii=False)
