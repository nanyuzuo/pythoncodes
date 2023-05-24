# 使用import导入openpyxl
import openpyxl
# 使用from...import从pyecharts.charts导入Boxplot
from pyecharts.charts import Boxplot
# 使用from...import从pyecharts导入options模块并简写为opts
from pyecharts import options as opts

# 将路径 /Users/panpan/测试数据.xlsx 赋值给path
path = "/Users/panpan/测试数据.xlsx"
# 使用 openpyxl.load_workbook() 读取文档，赋值给wb
wb = openpyxl.load_workbook(path)
# 使用 wb[] 读取"使用时长"赋值给user_time
user_time = wb["使用时长"]

# 定义函数 read_time() ，传入参数row
def read_time(row):
    # 使用工作表[]读取行数据赋值给rowData
    rowData = user_time[row]
    # 定义列表 timeList
    timeList = []
    # 使用for循环从第2个元素（索引为1）开始遍历
    for cell in rowData[1:]:
        # 使用 .value 获取单元格的内容赋值给time
        time = cell.value
        # 判断表内数据为空时，就跳过
        if time == None:
            continue
        # 使用append()将时间追加到列表中
        timeList.append(time)
    # 使用return返回列表timeList的值
    return timeList

# TODO 新建列表control_gp
control_gp = []
# TODO 新建列表exp_gp
exp_gp = []
# 使用for循环配合range()遍历2～8
for row in range(2,9):
    # TODO 调用read_time()函数，将返回值赋值给result
    result = read_time(row)
    # TODO 使用append()将返回值追加到列表control_gp中
    control_gp.append(result)

    # TODO 调用read_time()函数，传入参数row+10，将返回值赋值给exp_result
    exp_result = read_time(row+10)
    # TODO 使用append()将返回值追加到列表exp_gp中
    exp_gp.append(exp_result)

# 使用Boxplot()创建实例，赋值给boxplot
boxplot = Boxplot()

# 使用add_xaxis()设置横坐标
# 传入列表["第一天", "第二天", "第三天", "第四天", "第五天", "第六天", "第七天"]
boxplot.add_xaxis(xaxis_data=["第一天", "第二天", "第三天", "第四天", "第五天", "第六天", "第七天"])

# TODO 使用add_yaxis()函数设置y轴
# 将参数series_name设置为对照组
# 使用prepare_data()对control_gp进行处理，赋值给y_axis
boxplot.add_yaxis(series_name="对照组",y_axis=boxplot.prepare_data(control_gp))
# TODO 使用add_yaxis()函数设置y轴
# 将参数series_name设置为实验组
# 使用prepare_data()对exp_gp进行处理，赋值给y_axis
boxplot.add_yaxis(series_name="实验组",y_axis=boxplot.prepare_data(exp_gp))
# TODO 初始化一个TitleOpts对象，设置标题名称为"用户使用时长对比"，赋值给变量title_opts
# 使用set_global_opts()设置标题
boxplot.set_global_opts(title_opts=opts.TitleOpts(title="用户使用时长对比"))

# TODO 使用render()生成文件保存到/Users/panpan/abtest.html
boxplot.render("/Users/panpan/abtest.html")