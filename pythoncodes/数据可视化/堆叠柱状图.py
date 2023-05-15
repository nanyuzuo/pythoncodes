# TODO 从pyecharts.charts中导入Bar
from pyecharts.charts import Bar

# TODO 从pyecharts导入options,简称为opts
from pyecharts import options as opts

# 设置列表
months = ["7月", "8月", "9月", "10月", "11月", "12月"]
choc_sales=[5340,6078,6460,6475,7431,8038]
gum_sales=[4340,4379,4460,5075,5431,6038]
walnut_sales=[6340,5579,4460,4075,3431,3038]

# TODO 创建Bar对象，赋值给变量bar
bar = Bar()

# TODO 使用add_xaxis()函数，添加参数xaxis_data，将参数值设置为months
bar.add_xaxis(months)

# TODO 将数据标签配置项opts.LabelOpts()，赋值给变量label_options
# 在数据标签配置项中添加参数position，设置为"inside"
label_options = opts.LabelOpts(position="inside")

# TODO 使用add_yaxis()函数
# 将图例设置为“巧克力”
# y轴数值设置为列表choc_sales
# 添加参数stack，将值设置为sales
# 添加参数label_opts，将其值设置为label_options
bar.add_yaxis(series_name="巧克力",y_axis=choc_sales,stack="sales",label_opts=label_options)

# TODO 使用add_yaxis()函数
# 将图例设置为“口香糖”
# y轴数值设置为列表gum_sales
# 添加参数stack，将值设置为sales
# 添加参数label_opts，将其值设置为label_options
bar.add_yaxis(series_name="口香糖",y_axis=gum_sales,stack="sales",label_opts=label_options)

# TODO 使用add_yaxis()函数
# 将图例设置为“核桃”
# y轴数值设置为列表walnut_sales
# 添加参数stack，将值设置为sales
# 添加参数label_opts，将其值设置为label_options
bar.add_yaxis(series_name="核桃",y_axis=walnut_sales,stack="sales",label_opts=label_options)

# TODO 使用全局配置项，设置标题为"2020下半年商品销售额变化"
bar.set_global_opts(title_opts=opts.TitleOpts(title="2020下半年商品销售额变化"))

# TODO 使用render函数将堆积柱状图保存在指定路径
bar.render("d:\\yequ\\test\\bar_stack.html")