# 导入requests模块
import requests
# 导入bs4中的BeautifulSoup模块
from bs4 import BeautifulSoup
# 导入pandas模块并以pd调用
import pandas as pd

# 将User-Agent以字典键对形式赋值给headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

#  新建用于存储地区、部门、用人司局、职位名称的列表
areaList = []
departmentList =[]
companyList = []
positionList = []

# 使用for循环和range()生成1-5的变量并遍历
for page in range(1,6):
    
# 使用格式化组合链接
    url = f"https://nocturne-spider.baicizhan.com/practise/60/PAGE/{page}.html"
    # 使用get()函数请求链接，并且带上headers
    response = requests.get(url, headers=headers)
    # 使用.text属性将服务器相应内容转换为字符串形式，赋值给html
    html = response.text
    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html,"lxml")

# 是时候爬取网页表格数据了
    content_all = soup.tbody.find_all("tr")
    for item in content_all:
        area = item.contents[1].get_text()
        areaList.append(area)
        department = item.contents[3].get_text()
        departmentList.append(department)
        company = item.contents[5].get_text()
        companyList.append(company)
        position = item.contents[7].get_text()
        positionList.append(position)
writer = pd.ExcelWriter("d:\\yequ\\test\\公务员职位信息.xlsx")
total = {"地区":areaList,"部门":departmentList,"用人司局":companyList,"职位名称":positionList}
info = pd.DataFrame(total)
info.to_excel(excel_writer=writer,sheet_name="计算机科学与技术")
writer._save()