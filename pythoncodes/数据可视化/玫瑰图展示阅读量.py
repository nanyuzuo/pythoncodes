# TODO 从pyecharts.charts中导入Pie
from pyecharts.charts import Pie

# TODO 从pyecharts导入options,简称为opts
from pyecharts import options as opts

# 需要插入的数据
user_data = [('深度学习', 1000), ('数据分析', 700), ('Web开发', 500), ('爬虫开发', 350), ('图像处理', 250),('机器学习', 220),('数据挖掘', 200),('人工智能', 180),('自然语言处理', 160),('游戏开发', 140),('数据库开发', 120), ('可视化工程', 832)]

# TODO 按照列表中每个元组的第二个数据将元组从大到小排列
user_data = sorted(user_data,key=lambda item:item[1],reverse=True)

# TODO 创建Pie对象赋值给pie
pie = Pie()

# TODO 使用add()设置饼状图的内容
# 添加参数series_name，将图例设置为空
# 添加参数data_pair，将值设置为user_data
# 添加参数label_opts，将值设置为opts.LabelOpts
# 在数据标签配置项中添加参数formatter，将值设置为"{b}: {d}%"
# 添加参数rosetype，值设置为"area"
pie.add(series_name="",
        data_pair=user_data,
        label_opts=opts.LabelOpts(formatter="{b}: {d}%"),
        rosetype="area"
)
# 使用全局配置项，设置标题为"阅读量统计"
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="阅读量统计")
    )

# 使用render保存饼状图到指定路径
pie.render("/Users/yequ/rose_pie.html")