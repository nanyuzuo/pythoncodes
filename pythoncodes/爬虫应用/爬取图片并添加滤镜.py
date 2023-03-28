# TODO 使用import导入requests模块
import requests
# TODO 使用from..import从bs4模块导入BeautifulSoup
from bs4 import BeautifulSoup
# TODO 使用from..import从PIL模块导入Image,ImageFilter
from PIL import Image,ImageFilter

# 将电影URL地址，赋值给变量url
url = "https://nocturne-spider.baicizhan.com/2020/08/20/photo/"
# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
# 将字典headers传递给headers参数，添加进requests.get()中，赋值给response
response = requests.get(url, headers=headers)
# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text
# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")
# TODO 使用find()查询soup中class="post-body"的节点，赋值给content_all
content_all = soup.find(class_="post-body")
# TODO 使用find_all()查询content_all中的"img"节点，赋值给img_all
img_all = content_all.find_all(name="img")

# 创建记录图片名字的变量imgName并赋值为1
imgName = 1

# TODO for循环遍历img_all
for file in img_all:
    
    # TODO 使用.attrs获取src对应的属性值，并赋值给imgUrl
    imgUrl = file.attrs["src"]
    # TODO 使用requests.get()请求图片链接，赋值给imgResponse
    imgResponse = requests.get(imgUrl)
    # TODO 使用.content属性将响应消息转换成图片数据，赋值给img
    img = imgResponse.content

    # TODO 使用with...as语句配合open()函数以"wb"方式打开文件
    # 用格式化将图片名字和.jpg格式组合
    with open(f"{imgName}.jpg","wb") as f:
        # TODO 使用write()将图片写入
        f.write(img)

    # TODO 使用Image模块中的open函数打开图片文件，赋值给img_before
    # 使用格式化将图片名字和.jpg格式组合
    img_before = Image.open(f"{imgName}.jpg")
    # TODO 使用filter()函，调用参数ImageFilter.EMBOSS，赋值给img_after
    img_after = img_before.filter(ImageFilter.EMBOSS)
    # TODO 使用save()函数保存改后的图片
    img_after.save(f"{imgName}.jpg")
    # 将记录图片名字的变量imgName值增加1
    imgName = imgName+1