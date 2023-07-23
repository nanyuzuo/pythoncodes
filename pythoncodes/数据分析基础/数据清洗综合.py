import pandas as pd
df = pd.read_csv("180101-190630交易数据.csv",index_col="id")

df["payment"] = df["payment"]/100
df["price"] = df["price"]/100
df["cutdown_price"] = df["cutdown_price"]/100
df["post_fee"] = df["post_fee"]/100
df["create_time"] = pd.to_datetime(df["create_time"])
df["pay_time"] = pd.to_datetime(df["pay_time"])
df.drop(index=df[df["order_id"].duplicated()].index,inplace=True)
df.drop(index=df[df["user_id"]<0].index,inplace=True)
df.drop(index=df[df["payment"]<0].index,inplace=True)

abnormalTime = df[df["create_time"]>df["pay_time"]]
df.drop(index=abnormalTime.index,inplace=True)

df.info()