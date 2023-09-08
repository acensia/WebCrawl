from pymongo import MongoClient
import os, glob, json
from helper import sort_path

client = MongoClient("mongodb+srv://sudo:sudo@atlascluster.e7pmjep.mongodb.net/")

fashion_set = client["fashion"].img
fashion_single = client["fashion"].single


male_ame = glob.glob(os.path.join("./only_url", "male", "americancasual", "*", "anno_added.json"))
male_ame.sort(key=lambda x : sort_path(x))

# for f in male_ame:
#     with open(f, 'r', encoding='utf-8') as j:
#         anno = json.load(j)
#     fashion_set.insert_one(anno)