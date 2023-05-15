# TODO 使用from...import从pyecharts.charts中导入Bar
from pyecharts.charts import Bar

# TODO 使用from...import从pyecharts模块中导入options简写为opts
from pyecharts import options as opts

# 将10位博主的姓名存入变量名为'name'的列表中
name=["一起画笔记","我是课代表","菠萝冰和夏天","Jeannie花","Esther天","爱草莓的小挺","栀缘","钢琴上的音乐","Mu123","师008号"]

# 按照博主姓名的顺序，依次将博主的粉丝数量存入变量名为'fans'的列表中
fans=[12.5,23.1,38.5,15.8,14.1,11.4,18.2,16.5,22.6,32]

# 按照博主姓名的顺序，依次将博主的点赞收藏量存入变量名为‘likes’的列表中
likes=[18.2,15.2,222.7,71.5,8.6,70.5,107.7,128.3,109,31.7]

# TODO 使用Bar()函数创建对象并赋值给变量bar
bar = Bar()

# TODO 传入参数xaxis_data=name使用add_xaxis()设置x轴为博主名称
bar.add_xaxis(name)

# TODO 传入参数y_axis=fans使用add_yaxis()设置y轴，series_name设置为"粉丝数"
bar.add_yaxis(series_name="粉丝数",y_axis=fans)

# TODO 传入参数y_axis=likes使用add_yaxis()设置y轴，series_name设置为"点赞数"
bar.add_yaxis(series_name="点赞数",y_axis=likes)


# TODO 使用set_global_opts配置，设置标签旋转45度，设置标题名称为"粉丝数和点赞数"
bar.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate":45}),title_opts=opts.TitleOpts(title="粉丝数和点赞数"))


# TODO 使用render()生成文件保存到"/Users/yoyo/bar.html"
bar.render("/Users/yoyo/bar.html")