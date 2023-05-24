# 使用import导入openpyxl模块
import openpyxl
# TODO 使用from...import从pyecharts.charts导入Sankey
from pyecharts.charts import Sankey

# 使用openpyxl.load_workbook(path)读取文件，赋值给wb
wb = openpyxl.load_workbook("/Users/panpan/sankey.xlsx")
# 使用中括号读取工作表对照组和实验组，赋值给sheet_A,sheet_B
sheet_A = wb["对照组"]
sheet_B = wb["实验组"]

# 定义函数gen_nodesandlinks()，传入参数sheet
def gen_nodesandlinks(sheet):
    # 定义标签数据列表，赋值给变量list_labels
    list_labels = []
    # 定义信息流列表，赋值给变量links
    links = []
    # TODO 通过for循环，读取sheet2-24行数据
    for row in sheet[2:24]:
        # TODO .value属性获取元组索引为0的单元格值，并用append()函数添加进list_labels
        list_labels.append(row[0].value)
        # .value属性获取元组索引为0的单元格值，并用append()函数添加进list_labels
        list_labels.append(row[1].value)
        # 定义字典，赋值给变量dic
        dic = {}
        # TODO .value属性获取元组索引为0的单元格值，为dic创建（"source":"标签名1"）键：值对
        dic["source"] = row[0].value
        # .value属性获取元组索引为1的单元格值，为dic创建（"target":"标签名2"）键：值对
        dic["target"] = row[1].value
        # .value属性获取元组索引为2的单元格值，为dic创建（"value":值）键：值对
        dic["value"] = row[2].value
        # 使用append()函数将dic添加进links
        links.append(dic)

    # TODO 使用set()函数对list_labels去重
    # 使用list()函数对去重后的结果转化为列表
    # 赋值给变量list_nodes
    list_nodes = list(set(list_labels))

    # 定义节点列表，赋值给变量nodes
    nodes = []
    # TODO 通过for循环遍历list_nodes
    for i in list_nodes:
        # 定义字典，赋值给变量dic
        dic = {}
        # TODO 为dic创建（"name":"标签名"）键：值对
        dic["name"] = i
        # 使用append()函数将dic添加进nodes
        nodes.append(dic)

    # 使用return返回(nodes,links)
    return (nodes,links)

# 使用Sankey()函数创建对象赋值给sankey
sankey = Sankey()

# 传入sheet_B参数调用gen_nodesandlinks()，赋值给变量nodes_links
nodes_links = gen_nodesandlinks(sheet_B)

# TODO 为创建的实例增加图例名称"sankey"、传入节点和信息流列表
sankey.add("sankey",nodes_links[0],nodes_links[1])



# 使用render()生成桑基图保存到/Users/panpan/sankey.html
sankey.render("/Users/panpan/sankey.html")