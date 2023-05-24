# 从pyecharts.charts中导入Bar，Line，Pie，Map,Page
from pyecharts.charts import Bar,Line,Pie,Map,Page
# 从pyecharts中导入options简写为opts
from pyecharts import options as opts
# 列表month存储月份数据
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# 列表sale存储销售额数据
sale = [220,370,800,400,220,150,130,260,130,130,110,190]
# 将苹果，香蕉，核桃这三种水果12个月的库存数据分别存入列表stock_apple，stock_banana，stock_walnut中
stock_apple = [40,30,50,70,40,50,60,70,50,40,50,40]
stock_banana = [60,70,90,80,60,80,100,80,90,60,50,40]
stock_walnut = [50,40,60,70,60,70,80,65,70,60,80,50]
# 将三种水果的销售占比存储到列表data中
data = [("苹果", 40), ("香蕉", 20), ("核桃", 40)]
# 将水果销售地和销量信息存储到列表saleData中
saleData = [('安徽', 521), ('北京', 918), ('福建', 345), ('甘肃', 545), ('广东', 766), ('广西', 257), ('贵州', 185), ('海南', 86), ('河北', 327), ('河南', 336), ('黑龙江', 172), ('湖北', 522), ('湖南', 508), ('吉林', 497), ('江苏', 492), ('江西', 374), ('辽宁', 358), ('内蒙古', 100), ('宁夏', 84), ('青海', 97), ('山东', 508), ('山西', 266), ('陕西', 334), ('上海', 324), ('四川', 758), ('天津', 263), ('西藏', 62), ('新疆', 81), ('云南', 551), ('浙江', 500), ('重庆', 262)]
# TODO 创建Bar对象赋值给bar，将主题设置为dark，将图表宽度和高度都设置为"200px"
bar = Bar(init_opts=opts.InitOpts(theme="dark",width="200px",height="200px"))
# 使用add()函数添加x轴数据为month
bar.add_xaxis(xaxis_data = month)
# 使用add()函数添加y轴图例为"销售额"，数据为sale
bar.add_yaxis(series_name="销售额",y_axis = sale)
# 使用set_global_opts全局配置项，和DataZoomOpts区域缩放配置项，添加缩放滑块，设置参数is_show=True, type_="slider"
bar.set_global_opts(datazoom_opts=opts.DataZoomOpts(is_show=True, type_="slider"))

# TODO 创建一个折线图Line对象，并赋值给变量line，将主题设置为dark，将图表宽度和高度都设置为"200px"
line = Line(init_opts=opts.InitOpts(theme="dark",width="200px",height="200px"))
# 给折线图添加x轴数据，数据内容是month
line.add_xaxis(xaxis_data=month)
# 给折线图添加y轴数据，数据内容是苹果库存列表：stock_apple，图例名称为"苹果"
line.add_yaxis(series_name="苹果", y_axis=stock_apple)
# 给折线图添加y轴数据，数据内容是香蕉库存列表：stock_banana，图例名称为"香蕉"
line.add_yaxis(series_name="香蕉", y_axis=stock_banana)
# 给折线图添加y轴数据，数据内容是核桃库存列表：stock_walnut，图例名称为"核桃"
line.add_yaxis(series_name="核桃", y_axis=stock_walnut)
# 使用set_global_opts全局配置项，和DataZoomOpts区域缩放配置项，添加缩放滑块，设置参数is_show=True, type_="slider"
line.set_global_opts(datazoom_opts=opts.DataZoomOpts(is_show=True, type_="slider"))

# TODO 创建Pie对象赋值给pie，将主题设置为dark，将图表宽度和高度都设置为"200px"
pie = Pie(init_opts=opts.InitOpts(theme="dark",width="200px",height="200px"))

# 使用add()设置饼状图的内容
# 添加参数series_name，将图例设置为空
# 添加参数data_pair，将值设置为data
# 添加参数radius，将饼状图的半径设置为["40%","50%"]
pie.add(
    series_name="",
    data_pair=data,
    radius=["40%","50%"] 
    )
# TODO 创建Map对象赋值给mapChart，将主题设置为dark，将图表宽度和高度都设置为"200px"
mapChart = Map(init_opts=opts.InitOpts(theme="dark",width="200px",height="200px"))
# 使用add()设置地图的内容
# 添加参数series_name，将图例设置为空
# 添加参数data_pair，将值设置为saleData
# 添加参数maptype，将地图设置为"china"
mapChart.add(
    series_name = "",
    data_pair = saleData,
    maptype = "china"
)
# 使用set_global_opts全局配置项，和VisualMapOpts视觉映射配置项，添加视觉映射效果，并将最大值max设置为1000，
mapChart.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=1000))

# 创建Page对象赋值给page，设置布局模式为SimplePageLayout简单布局模式
page = Page(layout=Page.SimplePageLayout)
# 使用page.add()组合bar,line,pie,mapChart
page.add(pie,bar,line,mapChart)
# 使用render()函数，将图表保存到指定路径"/Users/fruit/show.html"
page.render("/Users/fruit/show.html")
