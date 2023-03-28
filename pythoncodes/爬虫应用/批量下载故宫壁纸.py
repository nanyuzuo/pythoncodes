import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

for page in range(1,4):
    pageurl = f"https://www.dpm.org.cn/lights/royal/p/{page}.html"
    response = requests.get(pageurl,headers=headers)
     #注意：下面一行手动制定了编码格式为"utf-8"(具体的编码格式在网页head中的charset有指定），
     # 这样做的目是避免alt属性文字变为乱码
    response.encoding='utf-8'
   
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    content_all = soup.find_all(class_="pic")
    for content in content_all:
        imgContent = content.find(name="img")
        imgUrl = imgContent.attrs["src"]
        imgTitle = imgContent.attrs["alt"]
        # imgName = str(count) + ".jpg"
        imgName = imgTitle + ".jpg"
        imgResponse = requests.get(imgUrl)
        img = imgResponse.content
        with open(f"d:\\test\\royal\\{imgName}","wb") as f:
            f.write(img)
        # count = count + 1
    print(f"第{page}页爬取完毕！")
print("全部壁纸爬取完毕")

