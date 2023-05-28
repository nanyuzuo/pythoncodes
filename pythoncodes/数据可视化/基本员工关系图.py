# 使用from...import从pyecharts.charts中导入Graph
from pyecharts.charts import Graph

# 使用from...import从pyecharts中导入options简写为opts
from pyecharts import options as opts

# 存储类别的列表category
category = [{"name":"舞蹈组"}, {"name":"声乐组"}]

# 存储基本新的列表info 
info = [ {"id":"Jon", "name":"Jon", "category":0, "symbolSize":50},
         {"id":"Jac", "name":"Jac", "category":1, "symbolSize":30},
         {"id":"Ten", "name":"Ten", "category":1, "symbolSize":10},
         {"id":"Bla", "name":"Bla", "category":1, "symbolSize":10},
         {"id":"Ann", "name":"Ann", "category":0, "symbolSize":10},
         {"id":"Ace", "name":"Ace", "category":0, "symbolSize":10},
         {"id":"Tom", "name":"Tom", "category":0, "symbolSize":10},
         {"id":"Gra", "name":"Gra", "category":0, "symbolSize":10}]

# 存储合作关系的列表coo
coo =  [ {"source":"Jon", "target":"Tom"},
         {"source":"Jon", "target":"Gra"},
         {"source":"Jon", "target":"Ace"},
         {"source":"Jon", "target":"Tom"},
         {"source":"Jac", "target":"Ten"},
         {"source":"Jon", "target":"Jac"},
         {"source":"Jac", "target":"Bla"},
         {"source":"Jon", "target":"Ann"}]

# 使用Graph()函数创建对象赋值给graph
graph = Graph()

# 调用add()函数，设置series_name为空
# 将category赋值给categories
# 将info赋值给nodes，将coo赋值给links
# 设置layout="circular"
# 设置is_rotate_label=True
# 调用LineStyleOpts()函数，传入参数color="source"，curve=0.3
graph.add(
    series_name="",
    categories=category,
    nodes=info,
    links=coo,
    layout="circular",
    is_rotate_label=True,
    linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3)
)

# 使用set_global_opts()函数进行全局配置
# TODO 使用TitleOpts()，设置标题为"员工合作关系图"，赋值给title_opts
graph.set_global_opts( title_opts=opts.TitleOpts(title="员工合作关系图"))

# 使用render()生成文件存储/Users/bing/graph.html
graph.render("/Users/bing/graph.html")