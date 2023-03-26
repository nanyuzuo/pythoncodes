# TODO 使用import导入requests模块
import requests

# TODO 使用from...import从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 将URL地址赋值给变量url
url = "http://nocturne.bczcdn.com/zip/1625207762993_63705/web.html"

# TODO 将变量url传入requests.get()，赋值给response
response = requests.get(url)

# TODO 使用.text将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# TODO 使用BeautifulSoup()读取html，添加lxml解析器，赋值给soup
soup = BeautifulSoup(html,"lxml")

# TODO 使用find_all()查询soup中class="rank"节点，赋值给content_all
content_all = soup.find_all(class_="rank")

# TODO for循环遍历content_all
for content in content_all:

    # TODO 使用find_all()查询name="a"的节点，赋值给title_list
    title_list = content.find_all(name="a")

    # TODO for循环遍历title_list
    for title in title_list:
        # TODO 使用print()输出标签中的内容
        print(title.string)