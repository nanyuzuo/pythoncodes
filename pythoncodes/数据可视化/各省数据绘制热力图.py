# 使用import导入openpyxl模块
import openpyxl

# TODO 从pyecharts.charts中导入HeatMap模块
from pyecharts.charts import HeatMap

# TODO 从pyecharts导入options,简称为opts
from pyecharts import options as opts

# 将文件路径/Users/feifei/三季度订单.xlsx，赋值给path
path = "/Users/feifei/三季度订单.xlsx"

# 使用openpyxl.load_workbook()读取文件，赋值给wb
wb = openpyxl.load_workbook(path)

# 使用中括号打开工作表"各省份每月销售额"，赋值给sheet_sales
sheet_sales = wb["各省份每月销售额"]

# 新建一个列表provinceList
provinceList = []

# for循环遍历sheet_sales第A列中第3行到第33行的单元格cell
for cell in sheet_sales["A"][2:33]:

    # 使用.value属性获取cell的值
    # 使用append()函数添加进列表provinceList
    provinceList.append(cell.value)

# TODO 新建一个列表month_sales_list
month_sales_list = []

# TODO for循环遍历sheet_sales中C3到E33的每一行rows
for rows in sheet_sales["C3:E33"]:

    # TODO for循环遍历rows中的每个单元格
    for cell in rows:

        # TODO 使用.value属性获取单元格的值
        # 使用append()函数将单元格的值添加到列表month_sales_list中
        month_sales_list.append(cell.value)

# TODO 新建列表heatmapList
heatmapList = []

# TODO 将变量n设置为0
n = 0

# TODO for循环遍历range()函数生成的0到30的数字column
for column in range(31):

    # TODO for循环遍历range()函数生成的0到2的数字row
    for row in range(3):

        # TODO 将变量column,row,索引列表month_sales_list第n项组成列表，赋值给heatmap_data
        heatmap_data = [column,row,month_sales_list[n]]

        # TODO 使用append()函数将heatmap_data添加进heatmapList
        heatmapList.append(heatmap_data)

        # TODO 将变量n进行累加
        n = n + 1

# TODO 创建一个HeatMap对象，赋值给heatmap
heatmap = HeatMap()

# TODO 使用add_xaxis()函数设置色块图x轴
# 添加参数xaxis_data，将参数值设置为列表provinceList
heatmap.add_xaxis(provinceList)

# TODO add_yaxis()函数设置色块图y轴
# 添加参数series_name，图例命名为空
# 添加参数yaxis_data，参数值为["7月","8月","9月"]
# 添加参数value,参数值为列表heatmapList
heatmap.add_yaxis(series_name="",
                  yaxis_data=["7月","8月","9月"],
                  value=heatmapList
)

# TODO 使用set_global_opts()设置全局配置
# 添加参数visualmap_opts，参数值为opts.VisualMapOpts()，将最大值设置为30000
# 添加xaxis_opts，参数值为opts.AxisOpts(),传入axislabel_opts={"rotate":45}
# 添加参数title_opts，参数值为opts.TitleOpts()
# 设置标题为"三季度各省份销售额"
heatmap.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=30000),
                        xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate":45}),
                        title_opts=opts.TitleOpts(title="三季度各省份销售额")
)

# TODO 使用render()函数保存并命名色块图
# 保存路径为"/Users/feifei/heatmap.html"
heatmap.render("/Users/feifei/heatmap.html")