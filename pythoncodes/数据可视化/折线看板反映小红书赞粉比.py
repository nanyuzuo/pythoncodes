# TODO 从pyecharts.charts中导入Line和Tab
from pyecharts.charts import Line,Tab
# TODO 从pyecharts中导入options模块并简写为opts
from pyecharts import options as opts
# TODO 创建一个组件Tab对象，赋值给变量tab
tab = Tab()
# 近10篇笔记的点赞量数据存入列表likes中
likes1 =[71,429,150,2214,626,1597,773,10000,1947,2275]
likes2 =[299,720,97,995,1010,12000,862,2588,1015,8522]
likes3 =[113,102,619,3465,531,1426,921,3717,2598,526]
likes4 =[421,392,680,938,2013,493,1624,1204,4955,2021]
likes5 =[151,376,60,3785,277,46,325,3212,143,566]
likes6 =[479,8355,933,3610,4073,606,1824,568,7981,632]

# 将博主姓名存入列表name_list中
name_list = ["菠萝冰和夏天","Jeannie花","爱草莓的小挺","栀缘","钢琴上的音乐","Mu123"]
# 将博主10篇笔记的点赞量数据存入列表likes_list中
likes_list =[likes1,likes2,likes3,likes4,likes5,likes6]

# 将最近10篇笔记的名字存入列表并赋值给变量page
page = ["近10篇","近9篇","近8篇","近7篇","近6篇","近5篇","近4篇","近3篇","近2篇","近1篇"]

# TODO 定义函数create_line()，获取博主名字name和点赞数likes，绘制折线图
def create_line(name,likes):
    # TODO 创建折线图Line对象，并赋值给变量line，设置主题为"dark"
    line = Line(init_opts=opts.InitOpts(theme="dark"))   
    # TODO 给折线图添加x轴数据，数据内容是笔记名字：page
    line.add_xaxis(page)   
    # TODO 给折线图添加y轴数据，数据内容是点赞量列表：likes，图例名称为博主姓名：name，折线图样式为：平滑折线图
    line.add_yaxis(series_name=name,y_axis=likes,is_smooth=True)                           
    # 用set_global_opts进行y轴配置，初始化一个AxisOpts对象，设置最大值为13000:
    line.set_global_opts(yaxis_opts= opts.AxisOpts(max_ = 13000))

    # 返回折线图
    return line

# 定义一个计数器n，初始值为0
n = 0
# 循环name_list列表，依次将博主name提取出来
for name in name_list:
    # 将create_line()函数赋值给line，参数为name，和列表likes_list中第n项的值
    line = create_line(name, likes_list[n])
    # TODO 使用tab.add()函数将折线图依次添加进看板中
    tab.add(line,name)
    # 计数器n加1
    n = n + 1

# TODO 使用tab.render()展示折线图，并保存到/Users/Yoyo/中，文件名称为line.html
tab.render("d:\\yequ\\test\\linetab.html")