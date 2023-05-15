# 定义未激活原因列表pointList
pointList = ['名字拼写错误', '地址错误', '电话号码错误', '邮箱错误', '验证码错误']
# 定义未激活数量列表scoreList
scoreList = [27, 16, 12, 9, 3]
# 定义累计频率列表percentList
percentList = [40.3, 64.18, 82.09, 95.52, 100.0]

# 绘制柱状图
# TODO 从pyecharts.charts中 导入 Bar模块
from pyecharts.charts import Bar
# TODO 从pyecharts中导入options模块，简写为opts
from pyecharts import options as opts
# TODO 创建一个柱状图Bar对象并赋值给变量bar
bar = Bar()
# TODO 使用add_xaxis函数，传入pointList作为x轴数据
bar.add_xaxis(pointList)
# TODO 使用add_yaxis函数，设置图例名称参数series_name为"原因"
# 传入scoreList作为y轴数据，透明度opacity设置为0.5
bar.add_yaxis(series_name="原因",y_axis=scoreList,itemstyle_opts=opts.ItemStyleOpts(opacity=0.5))

# TODO 使用全局配置项，设置标题为"信用卡未激活的原因"
bar.set_global_opts(title_opts=opts.TitleOpts(title="信用卡未激活的原因"))
# TODO 使用extend_axis函数，参数yaxis传入坐标轴配置项opts.AxisOpts()
bar.extend_axis(yaxis=opts.AxisOpts())
# 绘制折线图
# TODO 从pyecharts.charts中导入Line模块
from pyecharts.charts import Line
# TODO 创建一个折线图Line对象并赋值给变量line
line = Line()
# TODO 使用add_xaxis函数，传入pointList作为x轴数据
line.add_xaxis(pointList)
# TODO 使用add_yaxis函数，设置图例名称参数series_name为"原因占比(%)"
# 传入percentList作为y轴数据，设置yaxis_index为1
line.add_yaxis(series_name="原因占比(%)",y_axis=percentList,yaxis_index=1)

# TODO 对bar使用overlap()函数，传入line，就是在柱状图的基础上叠加折线图
bar.overlap(line)
# 绘制出图表/Users/baibai/credit_company.html
bar.render("/Users/baibai/credit_company.html")