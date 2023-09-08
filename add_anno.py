import os, glob, json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from helper import sort_path

def add_annotation(base_path, gender, chkpnt=0, chkstyle=None):
    # base_path, gender, style, number
    set_dirs = glob.glob(os.path.join(base_path, gender, "*", "*"))
    set_dirs.sort(key=lambda x: sort_path(x))
    driver = webdriver.Chrome()
    # wait = WebDriverWait(driver, timeout=2)

    for folder in set_dirs:
        with open(f"{folder}/anno.json", 'r', encoding='utf-8') as j:
            anno_d = json.load(j)
        fold = folder.split("\\")
        if chkstyle:
            if fold[2] < chkstyle:
                continue
            if fold[2] == chkstyle and int(fold[3]) < chkpnt:
                continue
        print(f"{fold[1]}, {fold[2]} : {fold[3]}")
        
        for i_d in anno_d["items"]:
            single_url = i_d["link"]
            driver.get(single_url)
            # time.sleep(0.4)
            try:
                alert = WebDriverWait(driver, 0.6).until(EC.alert_is_present())
                print("Alert found")
                i_d["alert"] = alert.text
                alert.accept()  # or you can use alert.dismiss() to cancel the alert
                continue
            except TimeoutException:
                # print("No alert found within the given time")
                pass
            
            
            texts = driver.find_elements(By.XPATH, '//p[@class="item_categories"]/a')
            img = driver.find_element(By.XPATH, '//div[contains(@class, "product-img")]/img') # not exact class name
            # wait.until(lambda d : img.is_displayed())
            i_d["url"] = img.get_attribute('src')
            i_d["type"] = texts[0].text
            if len(texts) < 2:
                continue
            i_d["label"] = texts[1].text

        with open(f"{folder}/anno_added.json", 'w', encoding='utf-8') as j:
            json.dump(anno_d, j, indent=4, ensure_ascii=False)
