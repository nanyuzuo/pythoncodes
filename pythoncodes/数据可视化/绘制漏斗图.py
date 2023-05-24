# 使用import导入openpyxl模块
import openpyxl
# TODO 使用from...import从pyecharts.charts中导入Funnel
from pyecharts.charts import Funnel
# TODO 使用from...import从pyecharts导入options，简写为opts
from pyecharts import options as opts

# 将文件路径赋值给path
path = "/Users/caicai/候选人跟进.xlsx"
# 使用openpyxl.load_workbook()读取文件，赋值给wb
wb = openpyxl.load_workbook(path)
# 使用中括号读取工作表岗位序列，赋值给positionSheet
positionSheet = wb["岗位序列"]

# 使用中括号读取第1行的数据赋值给label
label = positionSheet[1]
# 使用中括号读取第2行的数据赋值给num
num = positionSheet[2]
# 新建列表total
total = []
# 使用for循环和range()遍历1-6
for i in range(1,7):

    # 取label中的每项元素，使用.value得到值，赋值给title
    title = label[i].value
    # 取num中的每项元素，使用.value得到值，赋值给number
    number = num[i].value
    # 新建列表temp
    temp = []
    # 使用if判断i等于1时
    if i == 1:
        # 使用append()将title和100%追加到列表temp
        temp.append(title+"100%")
    # 否则
    else:
        # 使用(当前项/前一项)*100，赋值给pass_rate
        pass_rate = (number/num[i-1].value)*100
        # 使用round()保留pass_rate的一位小数，赋值给percent
        percent = round(pass_rate, 1)
        # 使用append()将标签和格式化组成的x%追加到列表temp
        temp.append(title+f"{percent}%")
    # 使用append()将number追加到列表temp
    temp.append(number)
    # 使用append()将temp追加到列表total
    total.append(temp)

# TODO 使用Funnel()函数创建对象赋值给funnel
funnel = Funnel()

# TODO 将series_name设为 漏斗图
# 将total赋值给data_pair
# 设置gap值为10
# 将参数添加到add()函数中
funnel.add(series_name="漏斗图",data_pair=total,gap=10)

# TODO 使用LegendOpts()，传入参数is_show=False，赋值给legend_opts 
# 使用TitleOpts()，设置标题为"产品岗位招聘情况"，赋值给title_opts
# 调用set_global_opts()
funnel.set_global_opts(legend_opts=opts.LegendOpts(is_show=False),title_opts=opts.TitleOpts(title="产品岗位招聘情况"))


# TODO 使用render()生成漏斗图，存到路径/Users/caicai/pm.html
funnel.render("/Users/caicai/pm.html")