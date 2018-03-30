# 切片可以指定步长
# 例如可以只取列表中的奇数部分（步长为2）
number=[1,2,3,4,5,6,7,8,9]
print(number[::2])

# 步长不能为0，否则无法向前移动，但可以为负数，即从右向左提取元素。
print(number[::-2])

# 可使用加法运算符来拼接序列  一般而言，不能拼接不同类
# 型的序列。

number_2=[10,11,12,13,14,15]
print(number+number_2)
# print(number+'hello')

# 将序列与数x相乘时，将重复这个序列x次来创建一个新序列
print('fyx'*34)
print(number*3)
print([2]*3)
print(['fyx']*34)
print(['']*4)
print([None]*5)