import json
import os

BASE_DIR = "json"

json_files = os.listdir(BASE_DIR)

image_urls = []
for json_file in json_files:
    data = json.load(open(os.path.join(BASE_DIR, json_file)))
    for url in data:
        if url["Image_URL"].find("data:image") == -1:
            image_urls.append(url)

json.dump(image_urls, open("json_extracted.json", "w"))