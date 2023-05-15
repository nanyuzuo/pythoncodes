# 从pyecharts.charts中导入Bar模块
from pyecharts.charts import Bar

# 从pyecharts导入options,简称为opts
from pyecharts import options as opts

# 设置列表
x_data = ["年初值","1月", "2月", "3月", "4月", "5月", "6月","7月", "8月", "9月", "10月", "11月", "12月","年末余值"]
y_total = ["-",5000,9000, 12450, 13500, 12000, 12000,21000,22300,23300,24400,20200,18690,"-"]
y_in = ["-",4000, 3450, 2850, "-", "-", 9000,1300,1000,2100,"-","-","-","-"]
y_out = ["-","-", "-", "-", 1800, 1500, "-","-","-","-",1000,4200,1510,"-"]
y_amount = [5000,"-","-","-","-","-","-","-","-","-","-","-","-",18690]

# TODO 创建Bar对象，赋值给变量bar
bar = Bar()

# TODO 使用add_xaxis()函数设置x轴，添加参数xaxis_data，将参数值设置为列表x_data
bar.add_xaxis(x_data)

# TODO 使用add_yaxis()函数
# 将图例设置为空
# y轴数值设置为列表y_total
# 添加参数color，设置颜色为白色"white"
# 添加参数stack，将值设置为"waterfall_plot"
bar.add_yaxis(series_name="",y_axis=y_total,color="white",stack="waterfall_plot")

# TODO 使用add_yaxis()函数
# 将图例设置为"收入"
# y轴数值设置为列表y_in
# 添加参数stack，将值设置为"waterfall_plot"
bar.add_yaxis(series_name="收入",y_axis=y_in,stack="waterfall_plot")

# TODO 使用add_yaxis()函数
# 将图例设置为"支出"
# y轴数值设置为列表y_out
# 添加参数stack，将值设置为"waterfall_plot"
bar.add_yaxis(series_name="支出",y_axis=y_out,stack="waterfall_plot")

# TODO 使用add_yaxis()函数
# 将图例设置为空
# y轴数值设置为列表y_amount
# 添加参数stack，将值设置为"waterfall_plot"
bar.add_yaxis(series_name="",y_axis=y_amount,stack="waterfall_plot")

# 使用全局配置项，设置标题为"下半年每月收入与支出"
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="下半年每月收入与支出"),
    xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate":45})
    )

# 将瀑布图保存至指定路径
bar.render("/Users/bar_waterfall_plot.html")