# 从pyecharts.charts中导入Pie
from pyecharts.charts import Pie

# 从pyecharts导入options,简称为opts
from pyecharts import options as opts

influencer_A = [("衬衫",111),("羊毛衫",122),("雪纺衫",113),("裤子",210), ("高跟鞋",170), ("袜子",109)]
influencer_B = [("衬衫",139),("羊毛衫",241),("雪纺衫",325),("裤子",260), ("高跟鞋",210), ("袜子",335)]

# TODO 创建Pie对象赋值给pie
pie = Pie()

# TODO 使用add()设置玫瑰图的内容
# 添加参数series_name，将图例设置为空
# 添加参数data_pair，将值设置为influencer_A
# 添加参数radius，将玫瑰图的半径设置为["20%", "60%"]
# 添加参数label_opts，将值设置为opts.LabelOpts
# 在数据标签配置项中添加参数formatter，将值设置为"{d}%"
# 添加参数position，将值设置为"inside"
# 添加参数rosetype，值设置为"area"
# 添加参数center，坐标设置为["25%", "50%"]
pie.add(series_name="",
        data_pair=influencer_A,
        radius=["20%","60%"],
        label_opts=opts.LabelOpts(formatter="{d}%",position="inside"),
        rosetype="area",
        center=["25%","50%"])
# TODO 使用add()设置玫瑰图的内容
# 添加参数series_name，将图例设置为空
# 添加参数data_pair，将值设置为influencer_B
# 添加参数radius，将玫瑰图的半径设置为["20%", "60%"]
# 添加参数label_opts，将值设置为opts.LabelOpts
# 在数据标签配置项中添加参数formatter，将值设置为"{d}%"
# 添加参数position，将值设置为"inside"
# 添加参数rosetype，值设置为"area"
# 添加参数center，坐标设置为["75%", "50%"]
pie.add(series_name="",
        data_pair=influencer_B,
        radius=["20%","60%"],
        label_opts=opts.LabelOpts(formatter="{d}%",position="inside"),
        rosetype="area",
        center=["75%","50%"])

# TODO 使用全局配置项，设置标题为"网络直播带货销量对比"
pie.set_global_opts(title_opts=opts.TitleOpts(title='网络直播带货销量对比'))

# 使用render保存玫瑰图到指定路径
pie.render("/Users/pie.html")