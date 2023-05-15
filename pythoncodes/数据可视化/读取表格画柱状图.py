# 使用import导入openpyxl模块
import openpyxl
# 使用from...import从pyecharts.charts导入Bar
from pyecharts.charts import Bar

# 将文件路径赋值给path
path = "/Users/caicai/候选人跟进.xlsx"
# 使用openpyxl.load_workbook()读取文件，赋值给wb
wb = openpyxl.load_workbook(path)
# 使用工作簿["工作表"]读取岗位序列，赋值给positionSheet
positionSheet = wb["岗位序列"]

# TODO 定义函数read_excel()传入参数row
def read_excel(row):
    # TODO 使用工作表+中括号读取行数据赋值给content
    content = positionSheet[row]
    # 定义列表y_list 
    y_list = []
    # 使用for循环遍历content[1:]，遍历的变量设为item
    for item in content[1:]:
        # 使用 .value 获取单元格的值，赋值给num
        num = item.value
        # 使用append()将num追加到列表中
        y_list.append(num)
    # TODO 使用return返回(行的名称,列表)
    return(content[0].value,y_list)

# 使用Bar()创建实例，赋值给bar
bar = Bar()

# TODO 使用for循环和range()遍历数字1-7
for i in range(1,8):
    # TODO 调用read_excel()函数，并将i传入，赋值给data
    data = read_excel(i)
    # 读取data的第一个元素赋值给name
    name = data[0]
    # 读取data的第二个元素赋值给num
    num = data[1]
    # TODO 使用if判断当i等于1时
    if i == 1:
        # TODO 传入参数xaxis_data=num，使用add_xaxis()设置x轴
        bar.add_xaxis(num)
    else:
        # TODO 将图例名name，赋值给series_name
        # 将y轴参数num，赋值给y_axis
        # 将参数依次传入add_yaxis()
        bar.add_yaxis(series_name=name,y_axis=num)

# TODO 使用render()生成柱状图
bar.render("/Users/caicai/total.html")