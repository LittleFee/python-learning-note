# 放在函数开头的字符串称为
# 文档字符串（docstring），将作为函数的一部分存储起来。
def fbnq(number):
    '生成斐波拉契数列，参数number生成的数列长度'
    number-=2
    lists = [0,1]
    for i in range(0,number):
        lists.append(lists[-1] + lists[-2])
    return lists
ls = fbnq(8)
print(ls)
# [0, 1, 1, 2, 3, 5, 8, 13]
print(fbnq.__doc__)
# 生成斐波拉契数列，参数number生成的数列长度

help(fbnq)

