# TODO 使用import导入requests模块
import requests

# TODO 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 将URL地址赋值给变量url
url = "https://nocturne-spider.baicizhan.com/2020/08/07/1/"

# TODO 将变量url传入requests.get()，赋值给response
response = requests.get(url)

# TODO 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# TODO 使用BeautifulSoup()读取html，添加lxml解析器，赋值给soup
soup = BeautifulSoup(html,"lxml")

# TODO 使用find_all()查询soup中em的节点，赋值给content_all
content_all = soup.find_all(name = "em")

# TODO for循环遍历content_all
for content in content_all:

    # TODO 获取每个节点中标签内的内容，赋值给contentString
    contentString = content.string
    
    # TODO 使用print输出contentString
    print(contentString)