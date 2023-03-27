# TODO 使用import导入requests模块
import requests

# TODO 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 使用import导入jieba模块
import jieba

# TODO 从collections中导入Counter模块
from collections import Counter

# TODO 将豆瓣评论URL地址，赋值给变量url
url = "https://nocturne-spider.baicizhan.com/practise/12.html"

# TODO 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# TODO 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url,headers=headers)

# TODO 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html,"lxml")

# TODO 使用find_all()查询soup中class="short"的节点，赋值给content_all
content_all = soup.find_all(class_="short")

# TODO 创建一个空白列表wordList
wordList = []

# TODO for循环遍历content_all
for content in content_all:

    # TODO 获取每个节点中标签内容，赋值给contentString
    contentString = content.string

    # TODO 使用jieba.lcut()将contentString进行分词，赋值给words
    words = jieba.lcut(contentString)

    # TODO 将列表wordList和列表words进行累加
    wordList = wordList + words

# TODO 使用Counter()函数统计wordList中的词语个数，赋值给word_counts
word_counts = Counter(wordList)

# TODO 使用word_counts.most_common()计算出现频率最高的10个单词，赋值给top_ten
top_ten = word_counts.most_common(10)

# TODO 使用print()输出结果
print(top_ten)