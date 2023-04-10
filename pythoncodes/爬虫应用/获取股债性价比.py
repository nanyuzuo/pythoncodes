import tushare as ts
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 登录Tushare账号
ts.set_token('0b99e2c05de16fec10076ebced34393706aa2bd6935c6629eeaf4637')
pro = ts.pro_api()

# 获取沪深300指数PE
df = pro.index_dailybasic(ts_code='000300.SH', fields='pe')
latest_pe = df['pe'].values[0]
print("Latest PE of HS300: {}".format(latest_pe))

# # 获取10年期国债收益率
# url = 'http://finance.sina.com.cn/bond/interest_rate.shtml'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# table = soup.find_all('table')[1]
# rate = table.find_all('tr')[1].find_all('td')[2].text.strip()
# print("10-year Treasury bond yield: {}%".format(rate))
