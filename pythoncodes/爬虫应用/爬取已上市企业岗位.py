import requests
from bs4 import BeautifulSoup
import time
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
for page in range(1,6):
    url = f"https://nocturne-spider.baicizhan.com/practise/42/PAGE/{page}.html"
    response = requests.get(url,headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    all_content = soup.find_all(class_="sojob-item-main clearfix")
    for content in all_content:
        if content.find(class_="field-financing").find(name="span").string == "已上市":
           company = content.find(class_="company-name").find(name="a").string
           job = content.find(class_="job-info").find(name="a").string.strip()
           jobUrl = content.find(class_="job-info").find(name="a").attrs["href"]
           with open("d:\\test\\工作数据.txt","a") as f: 
               f.write(company+","+job+","+jobUrl+"\n")
    print(f"第{page}页数据已爬取完成，稍等...")
    time.sleep(2)
print(f"前{page}页数据已全部爬取成功！")										