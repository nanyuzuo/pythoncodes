# TODO 使用import导入requests模块
import requests

# TODO 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 使用for循环遍历，range()函数生成的1-5的数字
for page in range(1,6):

    # TODO 利用格式化字符生成串网站链接，赋值给变量url
    url = f"https://ssr1.scrape.center/page/{page}"

    # TODO 将变量url传入requests.get()，赋值给response
    response = requests.get(url)

    # TODO 将服务器响应内容转换为字符串形式，赋值给html
    html = response.text

    # TODO 使用BeautifulSoup()读取html，添加lxml解析器，赋值给soup
    soup = BeautifulSoup(html,"lxml")

    # TODO 使用find_all()查询soup中h2的节点，赋值给name_all
    name_all = soup.find_all(name = "h2")

    # TODO for循环遍历name_all
    for movie in name_all:

        # TODO 获取每个节点中标签内的内容，赋值给name
        name = movie.string

        # TODO print输出name
        print(name)