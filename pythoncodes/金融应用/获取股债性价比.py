import pandas as pd
import tushare as ts
# 设置tushare API Key
# 通过账号访问数据源
token = "0b99e2c05de16fec10076ebced34393706aa2bd6935c6629eeaf4637"
pro = ts.pro_api(token)

# 获取沪深300指数的PE
df1 = pro.index_dailybasic(ts_code='000300.SH', fields='pe')
pe = df1.iloc[-1]['pe']  # 沪深300指数的PE（取最近一天的数据）

print(f"沪深300指数的PE为{pe:.2f}")  # 打印输出结果

# 获取国债收益率
df2 = pro.cn_macro_cnyc(ts_code='M0043803', fields='yc_rate')
rate = df2.iloc[-1]['yc_rate']  # 最新的十年期国债收益率（取最近一天的数据）

print(f"最新的十年期国债收益率为{rate:.2%}")