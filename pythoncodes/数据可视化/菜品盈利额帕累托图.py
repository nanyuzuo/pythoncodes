# 定义各菜品名字和其盈利额
dish_profit = {"番茄鸡蛋":9900,"避风塘茄夹":6660,"广东菜心":5210,"红烧肉":8880,"土豆烧排骨":2300,"木耳炒肉":1600,"虾仁蒸蛋":4280,"胡萝卜牛腩":3460,"水果沙拉":1800,"狮子头":3200}

# TODO 根据字典value的大小，对dish_profit的元素进行降序排序，然后结果赋值给result
result = sorted(dish_profit.items(),key=lambda item:item[1],reverse=True)

# 定义一个dishList和profitList的空列表
dishList = []
profitList = []

# for循环遍历列表result
for item in result:
    # 其中元组中第一个元素就是x轴的数据，添加到列表dishList中
    dishList.append(item[0])
    # 其中元组的第二个元素就是y轴的数据，添加到列表profitList中
    profitList.append(item[1])

# 定义一个累计频率的空列表percentlist
percentlist = []
# 定义一个计算累计频率的变量accu_percent，赋值为0
accu_percent = 0

# 遍历列表profitList中的每个元素
for profit in profitList:
    # 计算单个菜品占所有菜品的盈利额比例，乘100，赋值给percent
    percent = profit/sum(profitList)*100
    # 累计频率accu_percent，加上当前菜品的频率，得到当前的累计频率accu_percent
    accu_percent = accu_percent + percent
    # 使用round()函数保留两位小数，append到列表percentlist中
    percentlist.append(round(accu_percent,2))

# 绘制柱状图
# 从pyecharts.charts中 导入 Bar模块
from pyecharts.charts import Bar

# 从pyecharts中导入options模块，简写为opts
from pyecharts import options as opts

# 创建一个柱状图Bar对象并赋值给变量bar
bar = Bar()

# 使用add_xaxis函数，传入dishList作为x轴数据
bar.add_xaxis(xaxis_data=dishList)

# TODO 使用add_yaxis函数，设置图例名称参数series_name为"盈利额"
# 传入profitList作为y轴数据
bar.add_yaxis(series_name="盈利额",y_axis=profitList)

# 使用全局配置项，设置x轴旋转45度，设置标题为"各菜品盈利额"
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate":45}),
    title_opts=opts.TitleOpts(title="各菜品盈利额")
    )

# TODO 使用extend_axis函数，参数yaxis传入坐标轴配置项opts.AxisOpts()
bar.extend_axis(yaxis=opts.AxisOpts())

# 绘制折线图
# 从pyecharts.charts中导入Line模块
from pyecharts.charts import Line

# 创建一个折线图Line对象并赋值给变量line
line = Line()

# 使用add_xaxis函数，传入dishList作为x轴数据
line.add_xaxis(xaxis_data=dishList)

# TODO 使用add_yaxis函数，设置图例名称参数series_name为"盈利占比(%)"
# 传入percentlist作为y轴数据，设置yaxis_index为1，设置z_level为1
line.add_yaxis(series_name="盈利占比(%)",y_axis=percentlist,yaxis_index=1,z_level=1)

# TODO 对bar使用overlap()函数，传入line，就是在柱状图的基础上叠加折线图
bar.overlap(line)

# TODO 绘制出图表/Users/huahua/restaurant.html
bar.render("/Users/huahua/restaurant.html")