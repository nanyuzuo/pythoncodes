# TODO 使用import导入requests模块
import requests

# TODO 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 将豆瓣电影评论URL地址，赋值给变量url
url = "https://nocturne-spider.baicizhan.com/practise/7.html"

# TODO 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# TODO 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url,headers=headers)

# TODO 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html,"lxml")

# TODO 使用find_all()查询soup中class="title"的节点，赋值给content_all
content_all = soup.find_all(class_="title")

# TODO for循环遍历content_all
for content in content_all:
    # TODO 获取每个节点中标签内的内容，赋值给contentString
    contentString = content.string

    # TODO 使用if判断contentString等于"怦然心动"时
    if contentString == "怦然心动":
        # TODO 使用print()输出"怦然心动是豆瓣top25电影"
        print("怦然心动是豆瓣top25电影")