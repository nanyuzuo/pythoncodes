# 从pyecharts.charts中导入Bar模块
from pyecharts.charts import Bar
# 从pyecharts中导入options并简写为opts
from pyecharts import options as opts

# 创建变量x_data储存季度名称，作为x轴的数据
x_data = ["第一季度", "第二季度", "第三季度"]

# 将每个产业的每个季度的生产值保存在一个字典中
data = {"第一产业": [8014.7, 13992.8, 20528.5],
    "第二产业": [67968.9, 93094.8, 94684.4],
    "第三产业": [107685.8, 118408.4, 123963.2]}
  
# 创建一个Bar对象，并赋值给bar变量
bar = Bar()

# 调用add_xaxis方法添加x轴数据x_data
bar.add_xaxis(xaxis_data=x_data)

# TODO 使用for循环，遍历字典data中的key
for key in data.keys():
    # TODO 调用add_yaxis方法，series_name设置为字典的key，y_axis设置为key对应的value
    # 堆积名称设置为"GDP"
    # 使用opts.LabelOpts将标签的位置设置为"inside"
    bar.add_yaxis(
        series_name=key,
        y_axis=data[key],
        stack="GDP",
        label_opts=opts.LabelOpts(position="inside"))
        
# 设置全局配置项
# 将图表的标题设置为"2020年1-3季度GDP（单位：亿元）"
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="2020年1-3季度GDP（单位：亿元）")
    )

# 使用render方法生成图表，路径为GDP_plot.html
bar.render("/Users/yequ/GDP_plot.html")