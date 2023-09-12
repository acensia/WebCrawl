from pymongo import MongoClient
import os, glob, json
from helper import sort_path

client = MongoClient("mongodb+srv://sudo:sudo@atlascluster.e7pmjep.mongodb.net/")

fashion_set = client["fashion"].img
fashion_single = client["fashion"].top
fashion_bot = client["fashion"].bottom

def make_set():
    male_ame = glob.glob(os.path.join("./only_url", "female", "americancasual", "*", "anno_added.json"))
    male_ame.sort(key=lambda x : sort_path(x))

    for f in male_ame:
        with open(f, 'r', encoding='utf-8') as j:
            anno = json.load(j)
        fashion_set.insert_one(anno)
        # items = anno["items"]
        # for i in items:
        #     if i["type"] == "상의":
        #         fashion_set.insert_one(i)
 
def make_folder():
    client["fashion"].create_collection("bottom") 
 
        
def make_single():
    sams = fashion_set.find({}, {"_id":1, "items":1})
    singles = []
    bot = []
    for s in sams:
        top = s["items"]
        for t in top:
            t["root"] = s["_id"]
            if t["type"] == "상의":
                t["code"] = "001a2b"
                singles.append(t)
            if t["type"] in ["바지", "스커트"]:
                t["code"] = "001a2c"
                bot.append(t)
    fashion_single.insert_many(singles)
    fashion_bot.insert_many(bot)
    
    
make_single()
# make_folder()
# make_set()