# TODO 导入openpyxl模块
import openpyxl

# TODO 使用openpyxl.load_workbook()函数读取"2019年1月销售订单.xlsx"工作簿并赋值给变量wb 
# TODO 记得添加data_only=True参数打开工作簿，获取公式计算后的值
wb = openpyxl.load_workbook("2019年1月销售订单.xlsx",data_only=True)

# TODO 通过工作簿对象wb获取名为“销售订单数据”的工作表对象，并赋值给变量orderSheet
orderSheet = wb["销售订单数据"]

# TODO 定义一个空字典用来存储商品和其对应的销售额
sellData = {}

# TODO 遍历订单数据每一行
for row in orderSheet.rows:
    # TODO 取出第3列的商品名并赋值给productName
    productName = row[2].value
    
    # TODO 判断获取到的productName是"商品名"时
    if productName == "商品名":
        # TODO 使用continue跳过本行
        continue
    
    # TODO 获取订单总价I列的索引
    index = openpyxl.utils.cell.column_index_from_string("I") - 1
    # TODO 根据索引获取本行订单总价并赋值给变量price
    price = row[index].value
    
    # TODO 判断当商品名还不在结果字典sellData中时
    if productName not in sellData.keys():
        # TODO 给这个商品在sellData中设置初始值为0
        sellData[productName] = 0
    
    # TODO 将本行总价加到结果字典sellData对应商品名的销售额中
    sellData[productName] = sellData[productName] + price

# TODO 定义一个初始值为0的变量maxSold, 表示销售的最大值
maxSold = 0   
    
# TODO 定义一个空字符串变量maxName, 表示最大值的商品名
maxName = ""

# TODO 遍历结果字典sellData的键，也就是商品名
for productName in sellData.keys():
    # TODO 取出商品名对应的销售额赋值给变量productSold
    productSold = sellData[productName]
    
    # TODO 判断当前商品销售额大于记录的最大销售额maxSold时
    if  productSold > maxSold:
        # TODO 将maxSold替换成新的最大销售额
        maxSold = productSold
        # TODO 将maxName替换成新的最大销售额对应的商品名
        maxName = productName

# TODO 按格式输出结果: 明星产品是：{商品名}，一月总共销售出{最大销售额}元
print(f"明星产品是：{maxName}，一月总共销售出{maxSold}元")