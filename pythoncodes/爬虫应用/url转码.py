# TODO 使用import导入urllib.parse模块
import urllib.parse

# TODO 创建一个列表brandList，存储所有巧克力的品牌名字
bandList = ["德芙", "徐福记", "阿尔卑斯", "好时", "大白兔", "士力架", "不二家", "费列罗", "明治"]

# TODO 使用for循环遍历列表brandList中的每一项
for band in bandList:

    # TODO 使用urllib.parse.quote()函数，将中文转换成URL编码，赋值给chocolate
    chocolate = urllib.parse.quote(band)

    # TODO 利用格式化字符生成串网站链接 赋值给变量url
    url = f"https://search.jd.com/search?keyword={chocolate}&qrst=1&wq={chocolate}&stock=1"

    # TODO 使用print()输出url
    print(url)