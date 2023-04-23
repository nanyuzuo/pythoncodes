# TODO 从pyecharts.charts中导入Bar模块
from pyecharts.charts import Bar
# 导入requests模块
import requests
# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup
# 导入time模块
import time
# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
# 定义一个新函数getPositionInfo，包含参数detail_url
def getPositionInfo(detail_url):
    
    # 将detail_url和headers参数，添加进requests.get()中，给赋值给res
    res = requests.get(detail_url,headers=headers)

    # 使用.text属性获取网页内容，赋值给html
    html = res.text

    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    # 使用find()函数获取class="new_job_name"的节点
    # 使用attrs属性提取出title的属性值,赋值给变量job
    job = soup.find(class_="new_job_name").find(name = "span").string.strip()

    # 使用find()函数获取class="com-name"的节点
    # 使用.string属性提取出标签内容
    # 使用strip()移除空格，赋值给companyName
    companyName = soup.find(class_="com-name").string.strip()

    # 使用find()函数获取class="job_position"的节点
    # 使用.string属性提取出标签内容，赋值给position
    position = soup.find(class_="job_position").string

    # 使用find()函数获取class="job_money cutom_font"的节点
    # 使用.string属性提取出标签内容，赋值给salary
    salary = soup.find(class_="job_money cutom_font").string

    # # 使用encode()函数对变量salary编码，赋值给salary
    # salary = salary.encode()

    # # 使用replace()函数将二进制数据替换成UTF-8编码数字0-2
    # salary = salary.replace(b"\xee\x8b\xbf", b"0")
    # salary = salary.replace(b"\xee\xa2\x9c", b"1")
    # salary = salary.replace(b"\xee\x90\xb7", b"2")
    # # 使用replace()函数将二进制数据替换成UTF-8编码数字3-6
    # salary = salary.replace(b"\xee\x81\xa5", b"3")
    # salary = salary.replace(b"\xee\xad\xb1", b"4")
    # salary = salary.replace(b"\xee\xb2\xae", b"5")
    # salary = salary.replace(b"\xef\x8a\x98", b"6")
    # # 使用replace()函数将二进制数据替换成UTF-8编码数字7-9
    # salary = salary.replace(b"\xef\x80\xa6", b"7")
    # salary = salary.replace(b"\xee\xa1\xb1", b"8")
    # salary = salary.replace(b"\xee\xbe\xad", b"9")

    # # 使用decode()函数对替换后的二进制数据进行解码，赋值给salary
    # salary = salary.decode()
    
    # 使用with...as配合open()函数以a方式，打开路径为"/Users/tongtong/职位数据.txt"的文件，并赋值给f 
    with open("d:\\test\\tongtong\\职位数据.txt", "a") as f:
        # 使用write()函数写入job,companyName,position,salary
        # 变量之间以逗号相连，在数据末尾添加换行符
        f.write(job+","+companyName+","+position+","+salary+"\n")

# for循环遍历range()函数生成的1-6的数字
for i in range(1,6):

    # 利用格式化字符生成串网站链接 赋值给变量url
    url = f"https://www.shixiseng.com/interns?page={i}&type=intern&keyword=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&area=&months=&days=&degree=&official=entry&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
    
    # 将url和headers参数，添加进requests.get()中，将字典headers传递给headers参数，给赋值给res
    res = requests.get(url, headers=headers)
    
    # 使用.text属性获取网页内容，赋值给html
    html = res.text

    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html,"lxml")
    
    # 使用find_all()查询soup中class=title ellipsis font的节点，赋值给titles
    titles = soup.find_all(class_ = "title ellipsis font")

    # for循环遍历列表titles
    for item in titles:

        # 使用.attrs获取href对应的属性值，并赋值给detail_url
        detail_url = item.attrs["href"]

        # 调用getPositionInfo()函数，传入参数detail_url
        getPositionInfo(detail_url)
    
    # 使用time.sleep()停顿2秒
    time.sleep(2)
print("职位数据.txt文本文件保存完毕")
# TODO 使用with...as语句配合open()函数以r方式，打开路径为“/Users/tongtong/职位数据.txt”的文件，赋值给f
with open("d:\\test\\tongtong\\职位数据.txt","r") as f:

    # TODO 使用readlines()读取f中的所有行，赋值给dataList
    dataList = f.readlines()

# TODO 新建一个字典cityDict
cityDict = {}

# TODO for循环遍历列表dataList中的每个元素data
for data in dataList:

    # TODO 如果"薪资面议"在元素中
    if "薪资面议" in data:
        # TODO 就跳过
        continue

    # TODO 使用split()以逗号分隔data，索引第3项元素，赋值给city
    # 使用split()以逗号分隔data，索引第4项元素，赋值给salary
    # 使用split()以斜杠分隔salary，索引第1项元素，赋值给daily
    city = data.split(",")[2]
    salary = data.split(",")[3]
    daily = salary.split("/")[0]
    if "-" in daily:
        # TODO 使用split()以短横线分隔daily索引第1项，赋值给start
        # 使用split()以短横线分隔daily索引第2项，赋值给end
        start = daily.split("-")[0]
        end = daily.split("-")[1]
        
        # TODO 将start和end转换成整型相加后除以2，并赋值给average
        average = (int(start) + int(end)) / 2
    else:
        average = int(daily)

    # TODO 如果city不在字典cityDict的键中
    if city not in cityDict.keys():

        # TODO 将字典中键所对应的值设置为空列表
        cityDict[city] = []

    # TODO 使用append()函数往字典键所对应的值中添加average
    cityDict[city].append(average)

# TODO 新建一个字典city_num_dict
city_num_dict = {}

# TODO for循环遍历cityDict.items()中的key,value
for key,value in cityDict.items():

    # TODO 使用sum()函数将列表value求和
    # 使用len()函数计算列表value长度
    # 使用//运算符计算列表value的平均值，赋值给average_value
    average_value = sum(value) // len(value)

    # TODO 将字典cityDict的键对应的值设置为average_value
    cityDict[key] = average_value

    # TODO 将字典city_num_dict的键设置为不同城市
    # 将对应的值设置为len(value)
    city_num_dict[key] = len(value)

# TODO 创建Bar对象，赋值给bar
bar = Bar()

# TODO 使用list()将字典cityDict所有键转换成列表，传入add_xaxis()中
bar.add_xaxis(list(cityDict.keys()))

# TODO 使用add_yaxis()函数，将数据统称设置为"工资平均值"
# 将字典cityDict所有值转换成列表，作为参数添加进函数中
bar.add_yaxis("工资平均值",list(cityDict.values()))

# TODO 使用render()函数存储文件，设置文件名为salary.html
bar.render("d:\\test\\tongtong\\salary.html")

print("工资平均值柱状图生成完毕")

# TODO 创建Bar对象，赋值给bar_city
bar_city = Bar()

# TODO 使用list()将字典city_num_dict所有键转换成列表，传入add_xaxis()中
bar_city.add_xaxis(list(city_num_dict.keys()))

# TODO 使用add_yaxis()函数，将数据统称设置为"职位数量"
# 将字典city_num_dict所有值转换成列表，作为参数添加进函数中
bar_city.add_yaxis("职位数量",list(city_num_dict.values()))


# TODO 使用render()函数存储文件，设置文件名为positions.html
bar_city.render("d:\\test\\tongtong\\positions.html")

print("职位数量柱状图生成完毕")