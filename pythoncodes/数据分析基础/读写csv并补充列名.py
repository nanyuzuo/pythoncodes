# TODO 导入pandas模块
import pandas as pd

# TODO 使用pd.read_csv()函数、header参数和names参数
# 读取路径为"/Users/yequ/视频会员订单数据源.csv" 的CSV文件
# 并将数据的列名设置为: "order_id", "user_id", "price", "platform", "payment_provider", "create_time", "pay_time"
# 将结果赋值给变量data
data = pd.read_csv("/Users/yequ/视频会员订单数据源.csv",header=None,names=["order_id", "user_id", "price", "platform", "payment_provider", "create_time", "pay_time"])

# TODO 使用print()输出变量data
print(data)