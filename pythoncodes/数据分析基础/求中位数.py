# 创建列表Numbers
Numbers = [1, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 63, 64, 65, 67, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 959]

# TODO 使用len()函数获取列表Numbers的长度，并赋值给length
length = len(Numbers)

# 通过取模运算，判断length是奇数还是偶数
# TODO 如果取模运算返回余数为1，则长度是奇数
if length % 2 == 1:

    # TODO 通过整除运算，获取Numbers里中位数所在的索引，并赋值给n
    n = (length-1) // 2

    # TODO 通过索引[n]，获取Numbers的中位数，并赋值给Median
    Median = Numbers[n]

    # TODO 格式化输出：收入中位数为{Median}
    print(f"收入中位数为{Median}")


# TODO 否则，长度是偶数
else:

    # TODO 通过整除运算，获取Numbers里中间第二个数所在的索引，并赋值给n
    n = length // 2

    # TODO 通过索引[n-1]和[n]，获取Numbers里中间两个数，并计算它们的均值
    # 即中位数，将结果赋值给Median
    Median = (Numbers[n]+ Numbers[n-1])/2

    # TODO 格式化输出：收入中位数为{Median}
    print(f"收入中位数为{Median}")