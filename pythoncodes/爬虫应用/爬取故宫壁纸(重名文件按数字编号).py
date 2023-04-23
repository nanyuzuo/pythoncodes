# 是时候展示真正的技术啦
import requests
from bs4 import BeautifulSoup
import os
url = "https://nocturne-spider.baicizhan.com/practise/31.html"
def getImgContent(imgcontent):
    imgPageUrl = imgcontent.find(name="a").attrs["href"]
    imgResponse = requests.get(imgPageUrl)
    imgHtml = imgResponse.text
    soup2 = BeautifulSoup(imgHtml,"lxml")
    imgUrl = soup2.find(name="img").attrs["src"]
    return requests.get(imgUrl).content
    
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
soup1 = BeautifulSoup(html,"lxml")
content_all = soup1.find_all(class_="pic")
# 用字典来记录已经保存的文件名出现的次数
name_dict = {}
for content in content_all:
    imgTitle = content.find(name="img").attrs["alt"].replace(" ","_")
    # 组合图片文件名
    filename = imgTitle + ".jpg"
    # 记录文件名出现的次数
    if filename not in name_dict:
        name_dict[filename] = 0
    name_dict[filename] += 1
    if  name_dict[filename] == 1:
        img = getImgContent(content)
        # 写入图片文件
        with open(filename, "wb") as f:
            f.write(img)
        print(f"已成功保存{filename}")   
    if  name_dict[filename] > 1:
        if  os.path.exists(filename):
            os.rename(filename, f"{imgTitle}-1.jpg")
        filename_new = f"{imgTitle}-{name_dict[filename]}.jpg"
        img = getImgContent(content)    
        # 写入图片文件
        with open(filename_new, "wb") as f:
            f.write(img)
        print(f"已成功保存{filename_new}")
    
       
       
        
    