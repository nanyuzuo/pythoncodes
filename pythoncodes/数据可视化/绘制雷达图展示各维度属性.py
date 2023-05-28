# 使用from...import从pyecharts.charts导入Radar
from pyecharts.charts import Radar
# 使用import导入openpyxl模块
import openpyxl
# 从pyecharts导入options,简称为opts
from pyecharts import options as opts
# 将文件路径/Users/jiguang/yingxiong.xlsx，赋值给path
path = "/Users/jiguang/yingxiong.xlsx"
# 使用openpyxl.load_workbook()读取文件，赋值给wb
wb = openpyxl.load_workbook(path)
# 使用工作簿["工作表"]读取“筛选英雄”，赋值给sheet
sheet = wb["筛选英雄"]
# 新建一个列表data
data = []
# for循环遍历sheet第2-6行
for i in range(2,7):
    # 获取第i行的数据并赋值给
    row = sheet[i]
    # 新建一个列表
    num = []
    # for循环遍历第i行的第0-5列
    for n in range(0,6):
       # 使用.value获取第i行第n列单元格的值并赋值给cell
       cell = row[n].value
       # 使用append()将cell追加到列表num中
       num.append(cell)
    # 使用append()将num追加到列表data中
    data.append(num)

# 调用Radar()函数生成雷达图对象radar
radar = Radar()
# 构造坐标轴对象c_schema
c_schema = [
    # 以字典形式设置坐标轴名称"移动速度"和最大值10
    {"name": "移动速度", "max": 10},
    # 以字典形式设置坐标轴名称"生存能力"和最大值10
    {"name": "生存能力", "max": 10},
    # 以字典形式设置坐标轴名称"攻击伤害"和最大值10
    {"name": "攻击伤害", "max": 10},
    # 以字典形式设置坐标轴名称"技能效果"和最大值10
    {"name": "技能效果", "max": 10},
    # 以字典形式设置坐标轴名称"上手难度"和最大值10
    {"name": "上手难度", "max": 10}
]
# 在radar中使用add_schema()函数添加schema，设置坐标轴c_schema
# 将雷达图绘制类型设置为圆形shape="circle"
# 添加splitarea_opt，设置分隔区域的样式配置项为opts.SplitAreaOpts，传入is_show=True
# 添加areastyle_opts，设置区域填充样式配置项为opts.AreaStyleOpts，传入默认颜色的透明度为opacity = 1
radar.add_schema(schema = c_schema, shape = "circle",
    splitarea_opt=opts.SplitAreaOpts(
        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)))

# 在radar中使用add()函数添加系列名称data[0][0]、系列数据项[data[0][1:6]]和系列标签颜色color = "#800080"
# 添加areastyle_opts，设置区域填充样式配置项为opts.AreaStyleOpts，传入填充颜色的透明度为opacity = 0.1
radar.add(data[0][0], [data[0][1:6]], color = "#800080", areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),label_opts=opts.LabelOpts(is_show=False))

# 在radar中使用add()函数添加系列名称data[1][0]、系列数据项[data[1][1:6]]和系列标签颜色color = "#6495ed"
# 添加areastyle_opts，设置区域填充样式配置项为opts.AreaStyleOpts，传入填充颜色的透明度为opacity = 0.1
radar.add(data[1][0], [data[1][1:6]], color = "#6495ed", areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),label_opts=opts.LabelOpts(is_show=False))

# 在radar中使用add()函数添加系列名称data[2][0]、系列数据项[data[2][1:6]]和系列标签颜色color = "#696969"
# 添加areastyle_opts，设置区域填充样式配置项为opts.AreaStyleOpts，传入填充颜色的透明度为opacity = 0.1
radar.add(data[2][0], [data[2][1:6]], color = "#696969", areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),label_opts=opts.LabelOpts(is_show=False))

# 在radar中使用add()函数添加系列名称data[3][0]、系列数据项[data[3][1:6]]和系列标签颜色color = "#3cb371"
# 添加areastyle_opts，设置区域填充样式配置项为opts.AreaStyleOpts，传入填充颜色的透明度为opacity = 0.1
radar.add(data[3][0], [data[3][1:6]], color = "#3cb371", areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),label_opts=opts.LabelOpts(is_show=False))

# 在radar中使用add()函数添加系列名称data[4][0]、系列数据项[data[4][1:6]]和系列标签颜色color ="#ff8c00"
# 添加areastyle_opts，设置区域填充样式配置项为opts.AreaStyleOpts，传入填充颜色的透明度为opacity = 0.1
radar.add(data[4][0], [data[4][1:6]], color = "#ff8c00", areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),label_opts=opts.LabelOpts(is_show=False))

# TODO 使用set_global_opts()设置全局配置
# TODO 添加title_opts，设置标题配置项为opts.TitleOpts，传入title="性能展示"
radar.set_global_opts(title_opts=opts.TitleOpts(title="性能展示"))
# 使用render()函数生成雷达图，存到路径/Users/jiguang/yx.html
radar.render("/Users/jiguang/yx.html")