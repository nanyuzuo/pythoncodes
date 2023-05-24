# TODO 从pyecharts.charts导入Map
from pyecharts.charts import Map

# TODO 从pyecharts导入options,简称为opts
from pyecharts import options as opts

# 使用import导入openpyxl模块
import openpyxl

# 将文件路径"/Users/feifei/三季度订单.xlsx"，赋值给path
path = "d:\\yequ\\test\\三季度订单.xlsx"

# 使用openpyxl.load_workbook()读取文件，赋值给wb
wb = openpyxl.load_workbook(path)

# 使用中括号打开工作表"各省份付费用户数"，赋值给sheet_user
sheet_user = wb["各省份付费用户数"]

# 新建列表usersList
usersList = []

# for循环遍历range()函数生成的2-32的数字
for n in range(2,33):

    # 使用sheet_user[n]读取每一行的数据，赋值给province
    province = sheet_user[n]

    # 索引province的第一项和第二项
    # .value属性获取单元格值
    # 以元组的格式组合，赋值给data
    data = (province[0].value, province[1].value)
    
    # 使用append()函数将data添加进usersList
    usersList.append(data)

# TODO 创建Map对象赋值给变量mapChart
mapChart = Map()

# TODO 调用add()函数，添加参数series_name，参数值为空
# 添加参数data_pair，参数值为usersList
# 添加参数maptype，参数值为"china"
mapChart.add(series_name="",data_pair=usersList,maptype="china")

# TODO 使用set_global_opts()添加视觉映射配置项
# 添加参数visualmap_opts，参数值为opts.VisualMapOpts()
# 将最大值设置为 1000
# 添加参数title_opts，参数值为opts.TitleOpts()
# 设置标题为"三季度各省份付费用户数量"
mapChart.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=1000),title_opts=opts.TitleOpts(title="三季度各省份付费用户数量"))

# TODO 使用render()函数保存并命名地图
# 保存路径为"/Users/feifei/map.html"
mapChart.render("d:\\yequ\\test\\map.html")