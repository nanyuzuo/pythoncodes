# 使用import导入requests模块
import requests
# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将新闻URL地址，赋值给变量url
url = "http://nocturne.bczcdn.com/zip/1628129171125_75703/m.html"
# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
# 将字典headers传递给headers参数
# 将 url 和 headers参数，添加进requests.get()中，赋值给response
response = requests.get(url, headers=headers)
# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text
# 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# TODO 使用find_all()查询soup中class=tabContents active的节点，赋值给content_all
content_all = soup.find_all(class_="tabContents active")

# TODO 使用for循环遍历content_all中的每项
for content in content_all:

    # TODO 使用find_all()查询content中name="tr"的节点，赋值给all_title
    all_title = content.find_all(name="tr")

    # TODO 使用for循环遍历all_title中的每项
    for item in all_title:

        # TODO 使用find()查找item的a标签，判断为None时
        if item.find("a") == None:
            # TODO 继续下次循环
            continue
            
        # TODO 使用find()查找item的a标签，并用.string找到a标签中的文本，赋值给title
        title = item.find("a").string

        # TODO 使用find()查找item的a标签，并用.attrs获取a标签中href链接，赋值给title_url
        title_url = item.find("a").attrs["href"]

        # TODO 使用find()函数查找class="cBlue"的节点，并使用.string获取节点中的文本，赋值给likes
        likes = item.find(class_="cBlue").string

        # TODO 使用print()以格式化的方式输出 新闻标题 xxx 
        print(f"新闻标题 {title}")
        # TODO 使用print()以格式化的方式输出 点击量 xxx 
        print(f"点击量 {likes}")
        # TODO 使用print()以格式化的方式输出 链接 xxx + 换行
        print(f"链接 {title_url}"+"\n")