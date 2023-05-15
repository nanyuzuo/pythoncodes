# TODO 使用from...import从pyecharts.charts中导入Bar模块
from pyecharts.charts import Bar

# TODO 使用from...import从pyecharts中导入options模块并简写为opts
from pyecharts import options as opts

# 将公司的名字存入变量名为"name"的列表中
name = ["ibm","microsoft","pwc","citi","amazon","apple","ey","walmart","siemens","google"]
# 按照公司名字的顺序，依次将公司的人数存入变量名为"employee"的列表中
employee = [274047,116196,111372,101482,93247,90095,158363,120753,87381,75109]

# TODO 创建Bar对象，并赋值给bar
bar = Bar()

# TODO 传入参数xaxis_data=name使用add_xaxis()设置x轴为公司名称
bar.add_xaxis(name)

# TODO 传入参数y_axis=employee使用add_yaxis()设置y轴，series_name设置为空
bar.add_yaxis(series_name="",y_axis=employee)

# TODO 使用render()绘制柱状图保存到"/Users/company_size.html"
bar.render("d:\\yequ\\test\\company_size.html")