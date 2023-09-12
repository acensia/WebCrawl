from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import json



driver = webdriver.Chrome()

# driver.get("https://web.joongna.com/search?category=1068&page=1")




page = 1
total_sets = 0
limit = 200

sams = []
data = {}

idx = 0

while total_sets < limit:
    driver.get(f"https://web.joongna.com/search?category=1068&page={page}")
    ths = driver.find_elements(By.XPATH, '//img[@class="bg-gray-300 object-cover w-full transition duration-200 ease-in rounded-md group-hover:rounded-b-none"]')
    if len(ths) == idx:
        data["list"] = sams
        with open(f"./jungo_samples_{page}.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        page += 1
        idx = 0
        continue
    
    
    
    print(len(sams))
    cont = {}
    driver.execute_script("arguments[0].click();", ths[idx])
    time.sleep(0.8)
    sample = driver.find_element(By.XPATH, '//img[@class="object-cover w-full h-full rounded-lg top-1/2 left-1/2"]').get_attribute('src')
    name = driver.find_element(By.XPATH, '//h1[@class="flex justify-between mb-1 text-lg font-bold align-middle text-heading lg:text-xl 2xl:text-2xl hover:text-black"]').text
    cont["url"] = sample
    cont["name"] = name
    sams.append(cont)
    
    total_sets += 1
    idx += 1
    

driver.quit()