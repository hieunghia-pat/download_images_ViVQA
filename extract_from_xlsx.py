import pandas as pd
import json 
import os

BASE_DIR = "xlsx"
image_urls = []
for xlxs_file in os.listdir(BASE_DIR):
    items = pd.read_excel(os.path.join(BASE_DIR, xlxs_file))
    urls = items["Image_URL"].tolist()
    for url in urls:
        if not isinstance(url, str):
            continue
        if url.find("data:image") == -1:
            image_urls.append({
                "Image_URL": url
            })

json.dump(image_urls, open("xlxs_extracted.json", "w"))