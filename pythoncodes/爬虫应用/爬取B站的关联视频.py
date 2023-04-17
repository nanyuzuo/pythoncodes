import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
url = "https://nocturne-spider.baicizhan.com/practise/26.html"
response = requests.get(url,headers = headers)
html = response.text
soup = BeautifulSoup(html,"lxml")
allContent = soup.find_all(class_ = "info")
for content in allContent:
    text = content.find(name = "p")
    textContent = text.string
    url = content.find(name = "a")
    urlContent = url.attrs["href"]
    print(f"{textContent}:{urlContent}")
    