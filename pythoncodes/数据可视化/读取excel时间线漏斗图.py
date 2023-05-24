# 使用import导入openpyxl模块
import openpyxl
# TODO 使用from...import从pyecharts.charts
# 导入Timeline模块和Funnel模块
from pyecharts.charts import Timeline,Funnel

# 使用from...import从pyecharts导入options模块，简写为opts
from pyecharts import options as opts

# 将文件路径赋值给path
path = "/Users/caicai/候选人跟进.xlsx"
# 使用openpyxl.load_workbook()读取文件，赋值给wb
wb = openpyxl.load_workbook(path)
# 使用中括号读取工作表岗位序列，赋值给positionSheet
positionSheet = wb["岗位序列"]

# TODO 定义函数read_excel()传入参数row(行数)
def read_excel(row):
    # TODO 使用 工作表[] 读取第1行的数据赋值给label
    label = positionSheet[1]
    # TODO 使用 工作表[] 读取第row行的数据赋值给num
    num = positionSheet[row]
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
            # 使用append()将title和100%追击到列表temp
            temp.append(title+"100%")
        # 其他情况
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

    # TODO 使用return返回(num[0].value, total)
    return (num[0].value,total)

# TODO 使用Timeline创建对象赋值给tl
tl = Timeline()

# TODO 使用for循环配合range()函数遍历2～7
for i in range(2,8):
    # TODO 调用read_excel()函数，将参数i传入，赋值给data
    data = read_excel(i)

    # TODO 使用Funnel创建对象赋值给funnel
    funnel = Funnel()

    # TODO 将series_name设为空，data[1]赋值给data_pair，设置gap值为10
    # 将参数添加到add()函数中
    funnel.add(series_name="",data_pair=data[1],gap=10)

    # TODO 使用LegendOpts()，传入参数is_show=False，赋值给legend_opts 
    # 使用TitleOpts()，设置标题为"各岗位招聘转化率"，赋值给title_opts
    # 调用set_global_opts()
    funnel.set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                           title_opts=opts.TitleOpts(title="各岗位招聘转化率"))
    
    
    # TODO 将funnel赋值给chart，以格式化将f"{data[0]}岗位"赋值给time_point
    # 使用add()函数依次传入参数
    tl.add(chart=funnel,time_point=f"{data[0]}岗位")

# TODO 使用render()生成文件保存到/Users/caicai/position.html
tl.render("/Users/caicai/position.html")