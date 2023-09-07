import os
from module_crawl import crawl_style
from add_anno import add_annotation

# target styles
male_styles = ["americancasual","casual", "chic", "formal", "golf", "homewear", "sports", "street", "gorpcore", "dandy"]


base_path = "./only_url"
# os.makedirs(base_path, exist_ok=True)
    
# for st in male_styles:
#     crawl_style(st, base_path, "male")
#     print(f"male {st} completed")

add_annotation(base_path, "male")