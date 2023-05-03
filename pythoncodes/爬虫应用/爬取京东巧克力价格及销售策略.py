# 使用import导入requests模块
import requests
# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将User-Agent以字典键对形式赋值给headers，并加入cookie
headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
"cookie":"shshshfpa=59756f24-6de8-90a9-92f3-022a321cbcaa-1589969605; __jdu=1589969605288365795565; shshshfpb=fZNp5OzH0j2T%20X%20WnJhzrBg%3D%3D; qrsc=3; user-key=b05356ef-c40b-44d2-a837-60df17e9b74e; cn=0; _pst=jd_51aaae03cedfa; unick=jd_51aaae03cedfa; pin=jd_51aaae03cedfa; _tp=FNP1fTo2ON7jgdbikn0lWAbSqMI20pF0xO0Iq%2FccQVc%3D; pinId=qN40m03yULDpSLzjaHwm07V9-x-f3wj7; __jdc=122270672; rkv=1.0; 3AB9D23F7A4B3C9B=DVCEDHG6BLYWMZMJIWNBOSTWP7GOWK77C5VJKGVQO7F3JHUFZVL5V5B5UKDYLF2LK5VAEIOSN2YRG33EJLXR6ZJ2TU; __jdv=122270672|direct|-|none|-|1602475191357; areaId=22; ipLoc-djd=22-1930-50947-0; __jda=122270672.1589969605288365795565.1589969605.1602487075.1602569356.29; shshshfp=b393a5ab6c1163583435b3a90574cb22; shshshsID=ef428a912dae95ba61fd7ac2ee0af172_9_1602570753319; __jdb=122270672.9.1589969605288365795565|29.1602569356"}

# 使用for循环遍历range()函数生成的1-5的数字
for i in range(1, 6):
    # 使用格式化方法，将网址赋值给变量url
    url = f"https://nocturne-spider.baicizhan.com/practise/51/PAGE/{i}.html"
    response = requests.get(url,headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    content_all = soup.find_all(class_="gl-i-wrap")
    for content in content_all:
        price = content.find(class_="p-price").find("i").string
        title_all = content.find(class_="p-icons").find_all("i")
        titles = []
        for item in title_all:
            ptitle = item.text.replace("\n","").strip()
            titles.append(ptitle)
        title = " ".join(titles)
        print(f"价格:{price} 策略:{title}")
        
