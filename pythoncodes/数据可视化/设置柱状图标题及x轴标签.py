# TODO 导入options 模块并简写为opts
from pyecharts import options as opts
# TODO 从pyecharts.charts中 导入 Bar模块
from pyecharts.charts import Bar
# TODO 创建一个柱状图Bar对象并赋值给变量bar
bar = Bar()
# 将10位博主的姓名存入变量名为'name'的列表中
name=["一起画笔记","我是课代表","菠萝冰和夏天","Jeannie花","Esther天","爱草莓的小挺","栀缘","钢琴上的音乐","Mu123","师008号"]

# 按照博主姓名的顺序，依次将博主的粉丝数量存入变量名为'fans'的列表中
fans=[12.5,23.1,38.5,15.8,14.1,11.4,18.2,16.5,22.6,32]

# 按照博主姓名的顺序，依次将博主的点赞收藏量存入变量名为‘likes’的列表中
likes=[18.2,15.2,222.7,71.5,8.6,70.5,107.7,128.3,109,31.7]

# 计算点赞收藏量与粉丝量的比值
# 定义一个空列表ratioList，存储点赞收藏量与粉丝量的比值
ratioList = []
# 统计点赞收藏量列表长度，并赋值给length
length = len(likes)
# 将点赞收藏量列表中的值除以对应粉丝量列表中的值，并使用round()函数取近似值并保留2位小数,存储到ratioList列表中
for i in range(length):
    ratio = round(likes[i]/fans[i],2)
    ratioList.append(ratio)

# TODO 给柱状图添加x轴数据，数据内容是博主姓名列表：name
bar.add_xaxis(name)
# TODO 给柱状图添加y轴数据，数据内容是赞粉比列表：ratioList
bar.add_yaxis(series_name="赞粉比",y_axis=ratioList)
# 使用set_global_opts进行标题配置和x轴配置
# 初始化TitleOpts对象，设置标题名称为"候选博主粉丝与点赞的对比"
# 设置副标题名称为"筛选博主"
# TODO 初始化一个AxisOpts对象，设置标签旋转45度
bar.set_global_opts(title_opts=opts.TitleOpts(title = "候选博主粉丝与点赞的对比",subtitle = "筛选博主"),xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate":45}))

# TODO 绘制出这条柱状图，并保存到路径"/Users/Yoyo/Desktop/fans_likes.html"
bar.render("/Users/Yoyo/Desktop/fans_likes.html")