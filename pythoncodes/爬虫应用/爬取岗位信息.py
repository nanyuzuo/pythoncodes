# 导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 导入time模块
import time

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

# TODO for循环遍历range()函数生成的1-3的数字
for page in range(1,4):
    
    # TODO 用"https://nocturne-spider.baicizhan.com/practise/37/PAGE/"和page转换成的字符串格式相连，并赋值给url
    url = f"https://nocturne-spider.baicizhan.com/practise/37/PAGE/{page}.html"

    # TODO 将url和headers参数，添加进requests.get()中，将字典headers传递给headers参数，给赋值给res
    res = requests.get(url,headers=headers)

    # TODO 使用.text属性获取网页内容，赋值给html
    html = res.text

    # TODO 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html,"lxml")

    # TODO 使用find_all()查询soup中class=title的节点，赋值给content_all
    content_all = soup.find_all(class_="title")

    # TODO for循环遍历列表content_all
    for content in content_all:

        # TODO 使用.text获取每个节点中标签内的文本内容，赋值给title
        title = content.text

        # TODO 使用print输出title
        print(title)

    # TODO 使用time.sleep()停顿2秒
    time.sleep(2)