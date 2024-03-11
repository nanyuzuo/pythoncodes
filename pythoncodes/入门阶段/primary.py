# 最简单的输出
print("hello world")
# 输出变量
price = 10
number = 5
print(price,number)
print('总共花费',price*number)
# 使用sep分隔符
print('hello','world',sep=',')
print('2024','03','11',sep='-')
# 使用end,如不使用，python的默认end为\n(即换行)
print('hello',end=' ')
print('world')
# 换多行
print('hello',end='\n\n\n')
print('world')
# 使用file参数写入文件
file_source = open('zen.txt','w')
print('人生苦短，我用python',file=file_source)
file_source.close()


