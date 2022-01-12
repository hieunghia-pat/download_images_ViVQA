import json

image_urls = [url["Image_URL"] for url in json.load(open("json_extracted.json"))]
downloaded_image_urls = [url["Image_URL"] for url in json.load(open("xlxs_extracted.json"))]

remain_urls = []
image_urls = list(set(image_urls))
for url in image_urls:
    if url not in downloaded_image_urls:
        remain_urls.append({
            "Image_URL": url
        })

json.dump(remain_urls, open("extracted_url.json", "w"))