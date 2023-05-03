# 使用import导入requests模块
import requests
# 使用import导入json模块
import json

for i in range(0,5):
    page = i * 10
    url = f"https://spa1.scrape.center/api/movie/?limit=10&offset={page}"
    res = requests.get(url)
    html = res.text
    json_data = json.loads(html)
    data = json_data["results"]
    for content in data:
        name = content["name"]
        publish = content["published_at"]
        cover = content["cover"]
        print(f"{name} {publish} {cover}")