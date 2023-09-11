from pymongo import MongoClient
import os, glob, json
from helper import sort_path

client = MongoClient("mongodb+srv://sudo:sudo@atlascluster.e7pmjep.mongodb.net/")

fashion_set = client["fashion"].img
fashion_single = client["fashion"].top

def makeset():
    male_ame = glob.glob(os.path.join("./only_url", "male", "americancasual", "*", "anno_added.json"))
    male_ame.sort(key=lambda x : sort_path(x))

    for f in male_ame:
        with open(f, 'r', encoding='utf-8') as j:
            anno = json.load(j)
        items = anno["items"]
        # for i in items:
        #     if i["type"] == "상의":
        #         fashion_set.insert_one(i)
        
def make_single():
    sams = fashion_set.find({"items.type":"상의"}, {"_id":1, "items":1})
    singles = []
    for s in sams:
        top = s["items"]
        for t in top:
            if t["type"] == "상의":
                t["root"] = s["_id"]
                singles.append(t)
    fashion_single.insert_many(singles)
    
make_single()