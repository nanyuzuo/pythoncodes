# 从pyecharts.charts导入Map
from pyecharts.charts import Map
# 从pyecharts.charts中导入HeatMap模块
from pyecharts.charts import HeatMap
# 从pyecharts导入options,简称为opts
from pyecharts import options as opts
# 使用import导入openpyxl模块
import openpyxl

# 将文件路径"/Users/feifei/三季度订单.xlsx"，赋值给path
path = "/Users/feifei/三季度订单.xlsx"
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

# 创建Map对象赋值给变量mapChart
mapChart = Map()
# 调用add()函数，添加参数series_name，将图例设置为空
# 添加参数data_pair，参数值为usersList
# 添加参数maptype，参数值为"china"
mapChart.add(
    series_name="",
    data_pair=usersList,
    maptype="china"
    )
# 使用set_global_opts()添加视觉映射配置项
# 添加参数visualmap_opts，参数值为opts.VisualMapOpts()
# TODO 将最大值设置为 1000，将is_piecewise设置为True
# 添加参数title_opts，参数值为opts.TitleOpts()
# 设置标题为"三季度各省份付费用户数量"
mapChart.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(max_=1000, is_piecewise=True),
    title_opts=opts.TitleOpts(title="三季度各省份付费用户数量")
    )

# 使用中括号打开工作表"各省份每月销售额"，赋值给sheet_sales
sheet_sales = wb["各省份每月销售额"]
# 新建一个列表provinceList
provinceList = []
# for循环遍历sheet_sales第A列中第3行到第33行的单元格cell
for cell in sheet_sales["A"][2:33]:
    # 使用.value属性获取cell的值
    # 使用append()函数添加进列表provinceList
    provinceList.append(cell.value)
# 新建一个列表month_sales_list
month_sales_list = []
# for循环遍历sheet_sales中C3到E33的每一行rows
for rows in sheet_sales["C3:E33"]:
    # for循环遍历rows中的每个单元格
    for cell in rows:
        # 使用.value属性获取单元格的值
        # 使用append()函数将单元格的值添加到列表month_sales_list中
        month_sales_list.append(cell.value)

# 新建列表heatmapList
heatmapList = []
# 将变量n设置为0
n = 0
# for循环遍历range()函数生成的0到30的数字column
for column in range(31):
    # for循环遍历range()函数生成的0到2的数字row
    for row in range(3):
        # 将变量column,row,索引列表month_sales_list第n项组成列表，赋值给heatmap_data
        heatmap_data = [column,row,month_sales_list[n]]
        # 使用append()函数将heatmap_data添加进heatmapList
        heatmapList.append(heatmap_data)
        # 将变量n进行累加
        n = n + 1

# 创建一个HeatMap对象，赋值给heatmap
heatmap = HeatMap()
# 使用add_xaxis()函数设置色块图x轴
# 添加参数xaxis_data，将参数值设置为列表provinceList
heatmap.add_xaxis(xaxis_data=provinceList)
# add_yaxis()函数设置色块图y轴
# 添加参数series_name，图例命名为空
# 添加参数yaxis_data，参数值为["7月","8月","9月"]
# 添加参数value,参数值为列表heatmapList
heatmap.add_yaxis(
    series_name="",
    yaxis_data=["7月","8月","9月"],
    value=heatmapList
    )
# 使用set_global_opts()设置全局配置
# 添加参数visualmap_opts，参数值为opts.VisualMapOpts()，
# TODO 将最大值设置为30000，将is_piecewise设置为True
# 添加xaxis_opts，参数值为opts.AxisOpts(),传入axislabel_opts={"rotate":45}
# 添加参数title_opts，参数值为opts.TitleOpts()
# 设置标题为"三季度各省份销售额"
heatmap.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(max_=30000, is_piecewise=True),
    xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate":45}),
    title_opts=opts.TitleOpts(title="三季度各省份销售额")
    )

# 从pyecharts.charts导入Page模块
from pyecharts.charts import Page

# 创建Page对象，并赋值给page
# 添加参数layout，将参数值设置为Page.DraggablePageLayout
page = Page(layout=Page.DraggablePageLayout)

# 使用 add() 添加图表对象mapChart和heatmap
page.add(mapChart, heatmap)

# 使用render()函数保存并命名页面组合图表
# 保存路径为"/Users/feifei/page.html"
page.render("/Users/feifei/page.html")