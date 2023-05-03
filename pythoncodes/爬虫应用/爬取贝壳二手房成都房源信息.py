# 使用import导入requests模块
import requests
# 使用from...import从bs4模块中导入BeautifulSoup模块
from bs4 import BeautifulSoup
# 使用import导入time模块
import time
# 使用import导入pandas模块，并使用as简写为pd
import pandas as pd

# 将User-Agent以字典键对形式赋值给headers
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

writer = pd.ExcelWriter("d:\\yequ\\test\\二手房.xlsx")

totalPriceList = []
unitPriceList = []
areaList = []
communityInfoList = []
areaNameList = []
roomTypeList = []

def getDetailInfo(detail_url):
    response = requests.get(detail_url,headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    totalPrice = soup.find(class_="total").string
    totalPriceList.append(totalPrice)
    unitPrice = soup.find(class_="unitPriceValue").string
    unitPriceList.append(unitPrice)
    area = soup.select_one('.area > div:first-child').text
    areaList.append(area)
    communityInfo = soup.select_one('.communityName > a.info').text
    communityInfoList.append(communityInfo)
    areaName = soup.select_one('.info > a:first-child').text
    areaNameList.append(areaName)
    roomType = soup.find('span', string='房屋户型').next_sibling.strip()
    roomTypeList.append(roomType)

for page in range(1,6):
    time.sleep(2)
    url = f"https://cd.ke.com/ershoufang/pg{page}su1ie2sf1l2p5/"
    response = requests.get(url,headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    content_all = soup.find_all(class_="info clear")
    for item in content_all:
        detail_url = item.select_one('.title > a.VIEWDATA').attrs["href"]
        getDetailInfo(detail_url)   
total = {"房子总价/万":totalPriceList, "单价价格(元/平方)":unitPriceList, "建筑面积":areaList,"小区名称":communityInfoList,"所在区域":areaNameList,"房屋户型":roomTypeList}
info = pd.DataFrame(total)
info.to_excel(excel_writer=writer,sheet_name="成都")
writer._save()
