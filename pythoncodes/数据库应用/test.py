import requests
import json

url = '<http://push2ex.eastmoney.com/getStockFenShi?pageSize=1&pageNum=1&sort=1&date=&fqType=1&marketType=1&stockCode=000300&_=1613828031447>'
response = requests.get(url)
json_data = json.loads(response.text.lstrip('jsonp_callback(').rstrip(');'))
PE = json_data['data'][0]['f2']
print("沪深300的PE为:", PE)
