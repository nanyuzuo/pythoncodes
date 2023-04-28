# 从pyecharts.charts中导入Bar模块
from pyecharts.charts import Bar

# 从collections中导入Counter模块
from collections import Counter

# TODO 从collections中导入OrderedDict模块
from collections import OrderedDict

# 使用with...as语句配合open()函数以r方式，打开路径为“/Users/tongtong/职位数据.txt”的文件，赋值给f
with open("/Users/tongtong/职位数据.txt", "r") as f:

    # 使用readlines()读取f中的所有行，赋值给dataList
    dataList = f.readlines()

# 新建一个字典cityDict
companyDict = {}

# for循环遍历列表dataList中的每个元素data
for data in dataList:

    # 如果"薪资面议"在元素中
    if "薪资面议" in data:

        # 就跳过
        continue

    # 使用split()以逗号分隔data，索引第2项元素，赋值给company
    company = data.split(",")[1]

    # 使用split()以逗号分隔data，索引第4项元素，赋值给salary
    salary = data.split(",")[3]

    # 使用split()以斜杠分隔salary，索引第1项元素，赋值给daily
    daily = salary.split("/")[0]

    # 使用split()以短横线分隔daily索引第1项，赋值给start
    start = daily.split("-")[0]

    # 使用split()以短横线分隔daily索引第2项，赋值给end
    end = daily.split("-")[1]

    # 将start和end转换成整型相加后除以2，并赋值给average
    average = (int(start)+int(end))/2

    # 如果company不在字典companyDict的键中
    if company not in companyDict.keys():

        # 将字典中键所对应的值设置为空列表
        companyDict[company] = []

    # 使用append()函数往字典键所对应的值中添加average
    companyDict[company].append(average)

# for循环遍历companyDict.items()中的key,value
for key,value in companyDict.items():

    # 使用sum()函数将列表value求和
    # 使用len()函数计算列表value长度
    # 使用//运算符计算列表value的平均值
    average_value = sum(value)//len(value)

    # 将字典companyDict的键对应的值设置为average_value
    companyDict[key] = average_value

# TODO 使用Counter()函数统计companyDict中的薪资，赋值给salary_counts
salary_counts = Counter(companyDict)
print(type(salary_counts))
print(salary_counts)

# TODO 使用salary_counts.most_common()计算出现频率最高的7个单词，赋值给top_7_company
top_7_company = salary_counts.most_common(7)
print(type(top_7_company))
print(top_7_company)
# TODO 使用OrderedDict()函数将top_7_company转换成OrderedDict类型，赋值给sorted_companyDict
sorted_companyDict = OrderedDict(top_7_company)
print(type(sorted_companyDict))
print(sorted_companyDict)
# TODO 创建Bar对象，赋值给bar
bar = Bar()

# TODO 使用list()将字典sorted_companyDict所有键转换成列表，传入add_xaxis()中
bar.add_xaxis(list(sorted_companyDict.keys()))

# TODO 使用add_yaxis()函数，将数据统称设置为"公司"
# 将字典sorted_companyDict所有值转换成列表，作为参数添加进函数中
bar.add_yaxis("公司",list(sorted_companyDict.values()))

# TODO 使用render()函数存储文件，设置文件名为salary.html
bar.render("salary.html")