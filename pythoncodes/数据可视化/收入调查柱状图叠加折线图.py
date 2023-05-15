# 定义存储年龄区间，男性收入、女性收入和平均收入数据列表
ageList = ['<20', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '>=70']
male_salaryList = [145, 262, 367, 434, 498, 570, 623, 641, 616, 457, 379, 374]
female_salaryList = [106, 231, 295, 296, 292, 284, 286, 276, 261, 214, 205, 215]
average_salaryList = [125.5, 246.5, 331.0, 365.0, 395.0, 427.0, 454.5, 458.5, 438.5, 335.5, 292.0, 294.5]

# TODO 使用from...import从pyecharts.charts中导入Bar模块
from pyecharts.charts import Bar
# TODO 使用from...import从pyecharts中导入options模块，简写为opts
from pyecharts import options as opts

# TODO 使用Bar()函数创建对象并赋值给变量bar
bar = Bar()

# TODO 将年龄区间ageList传入add_xaxis()函数作为x轴数据
bar.add_xaxis(ageList)

# TODO 使用add_yaxis函数，设置图例名称参数series_name为"男性收入"，传入male_salaryList作为y轴数据
bar.add_yaxis(series_name="男性收入",y_axis=male_salaryList)

# TODO 使用add_yaxis函数，设置图例名称参数series_name为"女性收入"，传入female_salaryList作为y轴数据
bar.add_yaxis(series_name="女性收入",y_axis=female_salaryList)

# TODO 使用全局配置项，设置标题为"日本男女收入情况调查"
bar.set_global_opts(title_opts=opts.TitleOpts(title="日本男女收入情况调查")
    )

# TODO 使用from...import从pyecharts.charts中导入Line模块
from pyecharts.charts import Line

# TODO 创建一个折线图Line对象并赋值给变量line
line = Line()

# TODO 将年龄区间ageList传入add_xaxis()函数作为x轴数据
line.add_xaxis(ageList)

# TODO 使用add_yaxis函数，设置图例名称参数series_name为"平均收入"
# 传入average_salaryList作为y轴数据，设置z_level为1
line.add_yaxis(series_name="平均收入",y_axis=average_salaryList,z_level=1)

# TODO 对bar使用overlap()函数，传入line，就是在柱状图的基础上叠加折线图
bar.overlap(line)

# TODO 绘制出图表保存到路径"/Users/tangtang/salary.html"
bar.render("/Users/tangtang/salary.html")