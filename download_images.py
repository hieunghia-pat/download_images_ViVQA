from tqdm import tqdm
import os
import requests
import json
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("--from", type=int)
parser.add_argument("--to", type=int)

args = parser.parse_args()
args = vars(args)

image_urls = json.load(open("extracted_url.json"))
notfound_urls = []
ssl_error_urls = []

if not os.path.isdir("images"):
    os.mkdir("images")

image_id = args["from"] 
headers = {
            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
        }
for url in tqdm(image_urls[args["from"]:args["to"]]):
    url["Image_URL"] = re.sub(r":$", "", url["Image_URL"])
    try:
        response = requests.get(url["Image_URL"], stream=True, headers=headers)

        if not response.ok:
            print(f"{url['Image_URL']} - {response}")

        image_id += 1
        with open(os.path.join("images", f'image_{image_id}.jpg'), 'wb') as handle:
            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
    except:
        ssl_error_urls.append(url)
        print(f"Something happended while sending request to {url}")

if len(notfound_urls) > 0:
    json.dump(notfound_urls, open(f"not_found_url_{args['from']}_{args['to']}.json", "w"))

if len(ssl_error_urls) > 0:
    json.dump(ssl_error_urls, open(f"error_url_{args['from']}_{args['to']}.json", "w"))