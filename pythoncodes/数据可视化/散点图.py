# TODO 使用from...import从pyecharts.charts导入Scatter
from pyecharts.charts import Scatter
# 使用import导入openpyxl模块
import openpyxl
# 从pyecharts导入options,简称为opts
from pyecharts import options as opts
# 将文件路径/Users/jiguang/wj.xlsx，赋值给path
path = "/Users/jiguang/wj.xlsx"
# 使用openpyxl.load_workbook()读取文件，赋值给wb
wb = openpyxl.load_workbook(path)
#使用工作簿["工作表"]读取选手数据，赋值给sheet
sheet = wb["选手数据"]

# 新建一个列表list
List = []
# for循环遍历sheet第C列单元格cell
for cell in sheet["C"]:
# 使用.value属性获取cell的值
# 使用append()函数添加进列表List
    List.append(cell.value)
# 列表xdata
xdata = range(1,101)
# 列表TSdata
TSdata = List[1:101]
# 列表DXdata
DXdata = List[101:201]

# TODO 创建一个散点图Scatter对象并赋值给变量scatter
# 添加参数init_opts，设置标签配置项opts.InitOpts()，传入宽width="1000px", 高height="600px",主题theme="light"
scatter=Scatter(init_opts=opts.InitOpts(theme="light",width="1000px",height="600px"))
# 使用add_xaxis函数，传入xdata作为x轴数据
scatter.add_xaxis(xaxis_data = xdata)
# TODO 使用add_yaxis函数，设置图例名称为"TS"，传入TSdata作为y轴数据
# 添加参数label_opts，设置标签配置项opts.LabelOpts()，传入is_show=False
scatter.add_yaxis("TS",TSdata,label_opts=opts.LabelOpts(is_show=False))
# 使用add_yaxis函数，设置图例名称为"DX"，传入DXdata作为y轴数据
# 添加参数label_opts，设置标签配置项opts.LabelOpts()，传入is_show=False
scatter.add_yaxis("DX", y_axis = DXdata, label_opts=opts.LabelOpts(is_show=False))
# 使用set_global_opts()设置全局配置
scatter.set_global_opts(
    # TODO 添加xaxis_opts，设置坐标轴配置项opts.AxisOpts(),传入name="场次"
    xaxis_opts=opts.AxisOpts(name="场次"),
    # 添加yaxis_opts，设置坐标轴配置项为opts.AxisOpts(),传入name="KDA"
    yaxis_opts=opts.AxisOpts(name="KDA"),
    # TODO 添加title_opts，设置标题配置项为opts.TitleOpts，传入title="选手近100场比赛表现"
    title_opts=opts.TitleOpts(title="选手近100场比赛表现")
)
# 使用render()函数生成散点图，将文件存到路径/Users/jiguang/wj.html
scatter.render("/Users/jiguang/wj.html") 