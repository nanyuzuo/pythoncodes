import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

for page in range(1,4):
    pageurl = f"https://www.dpm.org.cn/lights/royal/p/{page}.html"
    response = requests.get(pageurl,headers=headers)
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    content_all = soup.find_all(class_="pic")
    for content in content_all:
        imgContent = content.find(name="img")
        # imgUrl = imgContent.attrs["src"]
        imgName = imgContent.attrs["alt"]
        print(imgName)
#         imgResponse = requests.get(imgUrl)
#         img = imgResponse.content
#         with open(f"d:\\test\\royal\\{imgName}","wb") as f:
#             f.write(img)
#     print(f"第{page}页爬取完毕！")
# print("全部壁纸爬取完毕")