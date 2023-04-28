# 使用import导入requests
import requests
# 使用from...import从bs4模块中导入BeautifulSoup
from bs4 import BeautifulSoup
# 使用from...import从pyecharts.charts导入Bar
from pyecharts.charts import Bar

# 将四川高考分数线链接"https://nocturne-spider.baicizhan.com/practise/44.html"赋值给url
url = "https://nocturne-spider.baicizhan.com/practise/44.html"
# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
# 将字典headers传递给headers参数
# 将 url 和 headers参数，添加进requests.get()中，赋值给response
response = requests.get(url, headers=headers)
# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text
# 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# 使用find_all()函数查找"table"标签，赋值给content_all
content_all = soup.find_all("table")

# 新建一个列表top用于存储一本分数线
top = []
# 新建一个列表basic用于存储二本分数线
basic = []

# TODO 使用for循环遍历content_all
for content in content_all:
    # TODO 使用find()查找class="c_blue"属性赋值给top_table
    top_table = content.find(class_="c_blue")
    # TODO 使用find_all()查找td标签，赋值给top_score
    top_score = top_table.find_all("td")
    # TODO 使用for循环遍历top_score
    for text in top_score:
        # TODO .string获取每个标签中的文本，并使用strip()去掉空格，赋值给score
        score = text.string.strip()
        # TODO 使用append()将数据追加到top列表中
        top.append(score)

    # TODO 使用find()查找class="c_white"属性赋值给basic_table
    basic_table = content.find(class_="c_white")
    # TODO 使用find_all()查找td标签，赋值给basic_score
    basic_score = basic_table.find_all("td")
    # TODO 使用for循环遍历basic_score
    for text in basic_score:
        # TODO .string获取每个标签中的文本，并使用strip()去掉空格，赋值给score
        score = text.string.strip()
        # TODO 使用append()将数据追加到basic列表中
        basic.append(score)

# TODO 生成横坐标年份的列表
# 新建一个列表，用于存储年份years
years = []
# TODO 使用for循环和range()遍历10-20的数字
for i in range(12,23):
    # TODO 使用格式化组合成 20xx ，赋值给year
    year = f"20{i}"
    # TODO 使用append()函数向years列表中追加年份
    years.append(year)
# TODO 使用reverse()函数将years列表进行逆序处理
years.reverse()

# 使用Bar()创建bar对象，赋值给bar
bar = Bar()
# 将获取的年份列表years传入add_xaxis函数
bar.add_xaxis(years)
# 将获取的数据切片后传入add_yaxis函数
# top和basic切片[1:12]是文科数据，[13:24]是理科数据
bar.add_yaxis('文科一本', top[1:12])
bar.add_yaxis('理科一本', top[13:24])
bar.add_yaxis('文科二本', basic[1:12])
bar.add_yaxis('理科二本', basic[13:24])
# 使用render()生成html，将文件存到路径 sc.html
bar.render("sc.html")