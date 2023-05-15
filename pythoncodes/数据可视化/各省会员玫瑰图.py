# 从pyecharts.charts中导入Pie模块
from pyecharts.charts import Pie
# 从pyecharts中导入options，简写为opts
from pyecharts import options as opts

# 所有省份的名称
data = {'北京': 78, '上海': 77, '黑龙江': 60, '吉林': 75, '辽宁': 91, '贵州': 93, '新疆': 82, '西藏': 61, '青海': 62, '四川': 40, '云南': 58, '陕西': 24, '重庆': 77, '内蒙古': 53, '广西': 46, '海南': 92, '澳门': 55, '湖南': 72, '江西': 65, '福建': 57, '安徽': 36, '浙江': 77, '江苏': 48, '宁夏': 32, '山西': 70, '河北': 86, '天津': 94}

# 这里已经帮你生成好了好看的颜色，直接使用pie.set_colors(color_series)即可设置颜色
color_series = ['#FAE927','#E9E416','#C9DA36','#9ECB3C','#6DBC49',
                '#37B44E','#3DBA78','#14ADCF','#209AC9','#1E91CA',
                '#2C6BA0','#2B55A1','#2D3D8E','#44388E','#6A368B',
                '#7D3990','#A63F98','#C31C88','#D52178','#D5225B',
                '#D02C2A','#D44C2D','#F57A34','#FA8F2F','#D99D21',
                '#CF7B25','#CF7B25','#CF7B25']


# TODO 使用sorted函数，将字典data按照value的大小降序排列
data = sorted(data.items(),key=lambda item:item[1],reverse=True)

# TODO 使用Pie()函数创建饼图对象赋值给变量pie
pie = Pie()
# TODO 设置颜色为color_series
pie.set_colors(color_series)

# TODO 给pie对象添加数据和配置
# 将series_name设置为会员地区分布
# 将data_pair设置为data
# 设置radius为30%到100%
# 设置rosetype参数为area
# 设置系列配置项label_opts，使用opts.LabelOpts将标签的position设为"inside"，将font_size设置为8，将格式formatter设置为"{b}:{c}人"
pie.add(series_name="会员地区分布",
        data_pair=data,
        radius=["30%","100%"],
        rosetype="area",
        label_opts=opts.LabelOpts(position="inside",font_size=8,formatter="{b}:{c}人")
        )
# 设置全局配置项
# 添加如表的标题为'会员地区分布'
# 设置图例不可见
pie.set_global_opts(
    title_opts=opts.TitleOpts(title='会员地区分布'),
    legend_opts=opts.LegendOpts(is_show=False)
    )

# 渲染在html页面上
pie.render('/Users/yequ/rose.html')