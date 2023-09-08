import os
from module_crawl import crawl_style
from add_anno import add_annotation

female_styles = ["americancasual","casual", "chic", "formal", "golf", "retro", "homewear", "sports", "street", "romantic", "girlish", "gorpcore"]


base_path = "./only_url"
# os.makedirs(base_path, exist_ok=True)
    
# for st in female_styles:
#     crawl_style(st, base_path, "female")
#     print(f"female {st} completed")
    

    
add_annotation(base_path, "female", chkstyle="casual", chkpnt=5)