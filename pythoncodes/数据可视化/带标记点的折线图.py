# 从pyecharts.charts中导入Line 
from pyecharts.charts import Line
# 使用from...import从pyecharts中导入options模块，并简写为opts
from pyecharts import options as opts

# 将三位主播的带货成交额数据存入下列列表中
huanhuan =[2.3, 2.3, 1.3, 1.2, 2.4, 3.6, 3.5, 3.4, 2.2, 5.5, 10.1, 9.2]
shushu =[5.2, 4.9, 4.6, 4.7, 4.4, 5.6, 5.5, 5.5, 4.1, 6.5, 5.0, 5.2]
binbin =[3.2, 3.3, 5.6, 5.4, 3.6, 4.2, 4.5, 2.5, 8.1, 8.6, 8.8, 6.3]

# 将12各月份并赋值给变量month
month = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]

# TODO 创建折线图Line对象，并赋值给变量line
line = Line()

# TODO 给折线图添加x轴数据，数据内容是月份：month
line.add_xaxis(month)

# TODO 给折线图添加y轴数据，数据内容是带货成交额数据：huanhuan，图例名称为主播名称：huanhuan，折线图样式为：平滑折线图，标记图形设置为circle，标记图形大小设置为10

line.add_yaxis(series_name="huanhuan",y_axis=huanhuan,is_smooth=True,symbol="circle",symbol_size=10)

# TODO 给折线图添加y轴数据，数据内容是带货成交额数据：shushu，图例名称为主播名称：shushu，折线图样式为：平滑折线图，标记图形设置为rect，标记图形大小设置为10
line.add_yaxis(series_name="shushu",y_axis=shushu,is_smooth=True,symbol="rect",symbol_size=10)


# TODO 给折线图添加y轴数据，数据内容是带货成交额数据：binbin，图例名称为主播名称：binbin，折线图样式为：平滑折线图，标记图形设置为triangle，标记图形大小设置为10
line.add_yaxis(series_name="binbin",y_axis=binbin,is_smooth=True,symbol="triangle",symbol_size=10)


# 初始化一个TitleOpts对象，设置标题title的值为"主播带货能力对比"，并将其赋值给变量title_options
title_options = opts.TitleOpts(title="主播带货能力对比")

# 使用set_global_opts进行标题配置，设置title_opts的值为title_options
line.set_global_opts(title_opts=title_options)

# 绘制出这条折线图，/Users/fanfan/line.html
line.render("/Users/fanfan/line.html")