# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 创建一个列表price_list
price_list = []

# TODO for循环遍历range()函数生成的1-3的数字
for page in range(1,4):

    # TODO 利用格式化字符生成串网站链接，赋值给变量url
    url = f"https://nocturne-spider.baicizhan.com/practise/40/PAGE/{page}.html"

    # 将User-Agent以字典键对形式赋值给headers
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

    # TODO 将url和headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
    response = requests.get(url,headers=headers)

    # TODO 将服务器响应内容转换为字符串形式，赋值给html
    html = response.text

    # TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html,"lxml")

    # TODO 使用find_all()查询soup中class="pirce"的节点，赋值给content_all
    content_all = soup.find_all(class_="pirce")

    # TODO for循环遍历content_all
    for content in content_all:

        # TODO 使用find()函数，找到<em>标签，并使用.string方法获取字符串，并赋值给price
        price = content.find(name = "em").string

        # TODO 使用float()函数将price转换成浮点型
        # 使用append()添加进price_list
        price = float(price)
        price_list.append(price)
        
# TODO 使用sum()函数将列表price_list求和
# 使用len()函数计算列表price_list长度
# 使用“/”计算平均数赋值给average
average = sum(price_list) / len(price_list)

# TODO 输出average
print(average)