# 从pyecharts.charts中导入Line和Tab
from pyecharts.charts import Line,Tab
# 从pyecharts中导入options模块，简写为opts
from pyecharts import options as opts
# 创建一个组件Tab对象，赋值给变量tab
tab = Tab()

# 将具体的气候数据存入下列列表中
Average_high =[8.1, 8.4, 11.3, 14.2, 17.9, 21.2, 23.5, 23.2, 20.2, 15.5, 11.1, 8.3]
Daily_mean =[5.2, 5.3, 7.6, 9.9, 13.3, 16.5, 18.7, 18.5, 15.7, 12.0, 8.0, 5.5]
Average_low =[2.3, 2.1, 3.9, 5.5, 8.7, 11.7, 13.9, 13.7, 11.4, 8.4, 4.9, 2.7]
Average_precipitation =[55.2, 40.9, 41.6, 43.7, 49.4, 45.1, 44.5, 49.5, 49.1, 68.5, 59.0, 55.2]
Average_ultraviolet_index =[1, 1, 2, 4, 5, 6, 6, 5, 4, 2, 1, 0]
Mean_monthly_sunshine_hours =[61.5, 77.9, 114.6, 168.7, 198.5, 204.3, 212.0, 204.7, 149.3, 116.5, 72.6, 52.0]

# 将气候数据的指标名称存入列表data_list中
data_list = ["Average high","Daily mean","Average low","Average precipitation","Average ultraviolet index","Mean monthly sunshine hours"]

# 将气候数据存入列表weather_list中
weather_list =[Average_high,Daily_mean,Average_low,Average_precipitation,Average_ultraviolet_index,Mean_monthly_sunshine_hours]

# 将12各月份并赋值给变量month
month = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]

# TODO 定义函数create_line()，获取气候数据的指标名称name和具体数据data，绘制折线图
def create_line(name,data):

    # TODO 创建折线图Line对象，并赋值给变量line
    line = Line()

    # TODO 给折线图添加x轴数据，数据内容是月份：month
    line.add_xaxis(month)

    # TODO 设置mark_opts，展示最大值，最小值
    mark_opts = opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), opts.MarkPointItem(type_="min")])
    
    # TODO 给折线图添加y轴数据，数据内容是气候数据：data，图例名称为气候数据的指标名称：name，并配置markpoint_opts
    line.add_yaxis(series_name=name,y_axis=data,markpoint_opts=mark_opts)

    # TODO 返回折线图
    return line

# TODO 定义一个计数器n，初始值为0
n = 0
# TODO 循环data_list列表，依次将气候数据的指标名称name提取出来
for name in data_list:
    # TODO 将create_line()函数赋值给line，参数为name，和列表weather_list中第n项的值
    line = create_line(name,weather_list[n])
    # TODO 使用tab.add()函数将折线图line和名称name，依次添加进看板中
    tab.add(line,name)
    # TODO 计数器n加1
    n = n + 1

# 使用tab.render()展示折线图，并保存到/Users/bingbing/weather.html
tab.render("/Users/bingbing/weather.html")
