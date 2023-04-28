# TODO 使用import导入requests模块
import requests

# TODO 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 将豆瓣电影评论URL地址，赋值给变量url
url = "https://nocturne-spider.baicizhan.com/practise/35.html"

# TODO 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# TODO 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url,headers=headers)

# TODO 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html,"lxml")

# TODO 使用find_all()查询soup中class="pl2"的节点，赋值给content_all
content_all = soup.find_all(class_="pl2")

# TODO for循环遍历content_all
for content in content_all:

    # TODO 使用.text方法获取content中a标签下的的text文本信息，赋值给title
    title = content.a.text

    # TODO 使用replace()去掉换行符
    title = title.replace("\n","")

    # TODO 使用replace()去掉空格
    title = title.replace(" ","")

    # TODO print书名
    print(title)