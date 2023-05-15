# 从pyecharts.charts中导入Line 
from pyecharts.charts import Line
# 从pyecharts中导入options模块，简写为opts
from pyecharts import options as opts

# 将周一至周日并赋值给变量data
data = ['周一','周二','周三','周四','周五','周六','周日']

# 将不同营销渠道的点击量数据存入下列列表中
email = [120, 132, 101, 134, 90, 230, 210]
video = [150, 232, 201, 154, 190, 330, 410]

# 创建折线图Line对象，并赋值给变量line
line = Line()

# TODO 给折线图添加x轴数据，数据内容是data
line.add_xaxis(data)

# TODO 给折线图添加y轴数据，数据内容是email，图例名称为：邮件营销，折线图样式为：平滑折线图，AreaStyleOpts配置项中opacity设置为0.5
line.add_yaxis(series_name="邮件营销",y_axis=email,is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5))

# TODO 给折线图添加y轴数据，数据内容是video，图例名称为：视频推广，折线图样式为：平滑折线图，AreaStyleOpts配置项中opacity设置为0.5
line.add_yaxis(series_name="视频推广",y_axis=video,is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5))

# 初始化一个TitleOpts对象，设置标题title的值为"营销渠道点击对比"，并将其赋值给变量title_options
title_options = opts.TitleOpts(title="营销渠道点击对比")

# 使用set_global_opts进行标题配置，设置title_opts的值为title_options
line.set_global_opts(title_opts=title_options)

# 绘制出这条折线图，/Users/tiantian/area.html
line.render("/Users/tiantian/area.html")