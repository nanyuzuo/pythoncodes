# TODO 从pyecharts.charts中导入Pie
from pyecharts.charts import Pie

# TODO 从pyecharts导入options,简称为opts
from pyecharts import options as opts

# 按照批评者、被动者和推荐者的顺序以元组的格式组成列表
# 赋值给 user_data
user_data = [("批评者",879),("被动者",440),("推荐者",1248)]


# TODO 创建Pie对象赋值给pie
pie = Pie()

# TODO 使用add()设置饼状图的内容
# 添加参数series_name，将图例设置为空
# 添加参数data_pair，将值设置为user_data
# 添加参数label_opts，将值设置为opts.LabelOpts
# 在数据配置项中添加参数formatter，将值设置为"{d}%"
# 添加参数position，将值设置为"inside"
# 添加参数radius，将饼状图的半径设置为40%
pie.add(series_name="",data_pair=user_data,label_opts=opts.LabelOpts(formatter="{d}%",position="inside"),radius="40%")

# TODO 使用全局配置项，设置标题为"购买核桃用户NPS占比"
pie.set_global_opts(title_opts=opts.TitleOpts(title="购买核桃用户NPS占比"))

# TODO 使用render保存饼状图到指定路径
pie.render("/Users/azhan/pie.html")
