import pymysql
from pyecharts import options as opts
conn = pymysql.connect(host='127.0.0.1', port = 3306, user='root', password='Ubuntu12.04', database='tushare')
cur = conn.cursor()
SQL1  = '''
SELECT ts_code, WEEKDAY(trade_date)+1 AS day_of_week, AVG((close - pre_close)*100/pre_close) AS 平均涨跌幅
FROM index_daily 
GROUP BY ts_code, WEEKDAY(trade_date)+1
ORDER BY ts_code, day_of_week
;'''
cur.execute(SQL1)
data = list(cur.fetchall())
cur.close()
conn.close()

name = ["上证综指", "上证50", "沪深300","中证500","深证成指"]
# 从pyecharts.charts中导入Line模块
from pyecharts.charts import Line
# 创建一个折线图Line对象并赋值给变量line
line=Line()
# 设置x轴数据
week = ['星期一','星期二','星期三','星期四','星期五']
# 给折线图添加x轴数据，数据内容是日期列表：week
line.add_xaxis(xaxis_data=week)
# TODO 新建一个变量ret存储获取的涨跌幅数据
ret = []
# TODO 使用append()方法提取data列表中第三项信息，存储到变量ret中
for i in data:
    ret.append(i[2])

# TODO 使用for循环遍历列表ret，每次提取5个数据，存储到变量r中
for i in range(5):

    # TODO 使用add_yaxis()方法添加y轴数据
    r = ret[i*5:(i+1)*5]
    line.add_yaxis(series_name = name[i],y_axis = r)

# TODO 使用set_series_opts方法设置隐藏标签
line.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

# TODO 使用render()函数存储图表)
line.render(r"d:\test\line.html")
