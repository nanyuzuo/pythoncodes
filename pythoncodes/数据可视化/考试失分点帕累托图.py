# 定义知识点和平均扣分的字典
knowledge = {"圆锥曲线":7.5,"直线与圆":5.0,"立体几何":10.1,"空间向量":3.2,"数列":14.5,"解三角":1.9,"导数":28.5,"函数模型":3.3,"二项式定理":3.0,"线性规划":4.0,"平面向量":3.5,"复数":1.3,"集合":1.9}

# 根据字典value的大小，对knowledge的元素进行降序排序，然后结果赋值给result
result = sorted(knowledge.items(),key = lambda item:item[1],reverse=True)

# 定义一个pointList和scoreList的空列表
pointList = []
scoreList = []

# for循环遍历列表result
for item in result:
    # 其中元组中第一个元素就是x轴的数据，添加到列表pointList中
    pointList.append(item[0])
    # 其中元组的第二个元素就是y轴的数据，添加到列表scoreList中
    scoreList.append(item[1])

# 定义一个累计频率的空列表percentlist
percentlist = []
# 定义一个计算累计频率的变量accu_percent，赋值为0
accu_percent = 0

# 遍历列表scoreList中的每个元素
for score in scoreList:
    # 计算单个扣分分数，占所有扣分分数的比例，乘100，赋值给percent
    percent = score/sum(scoreList)*100
    # 累计频率accu_percent，加上当前扣分分数的频率，得到当前的累计频率accu_percent
    accu_percent = accu_percent + percent
    # 使用round()函数保留两位小数，append到列表percentlist中
    percentlist.append(round(accu_percent,2))

# 绘制柱状图
# 从pyecharts.charts中 导入 Bar模块
from pyecharts.charts import Bar

# 创建一个柱状图Bar对象并赋值给变量bar
bar = Bar()

# 使用add_xaxis函数，传入pointList作为x轴数据
bar.add_xaxis(xaxis_data=pointList)

# 使用add_yaxis函数，设置图例名称参数series_name为"扣分"，传入scoreList作为y轴数据
bar.add_yaxis(
    series_name="扣分", 
    y_axis=scoreList
    )

# 从pyecharts中导入options模块，简写为opts
from pyecharts import options as opts

# 使用全局配置项，设置x轴旋转45度
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate":45}),
    # TODO 设置标题为"数学模块最薄弱的失分点"
    title_opts=opts.TitleOpts(title="数学模块最薄弱的失分点")
    )

# 使用extend_axis函数，参数yaxis传入坐标轴配置项opts.AxisOpts()
bar.extend_axis(yaxis=opts.AxisOpts())

# 绘制折线图
# 从pyecharts.charts中导入Line模块
from pyecharts.charts import Line

# 创建一个折线图Line对象并赋值给变量line
line = Line()

# 使用add_xaxis函数，传入pointList作为x轴数据
line.add_xaxis(xaxis_data=pointList)

# 使用add_yaxis函数，设置图例名称参数series_name为"扣分占比"，传入percentlist作为y轴数据，设置yaxis_index为1，设置z_level为1
line.add_yaxis(
    series_name="扣分占比",
    y_axis=percentlist,
    yaxis_index=1,
    z_level=1
    )

# 对bar使用overlap()函数，传入line，就是在柱状图的基础上叠加折线图
bar.overlap(line)

# 绘制出图表
bar.render("d:\\yequ\\test\\pareto_overlap.html")