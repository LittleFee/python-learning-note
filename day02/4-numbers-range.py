for number in range(1,5) :
    print(number)

# 函数range(start,end)让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，
# 因此输出不包含第二个值（这里为5）。
# 这里如果想要打印1-5则range(1,6)

for number in range(1,6) :
    print(number)

print('------')
# 要创建数字列表，可使用函数list()将range()的结果直接转换为列表。
# 如果将range()作为list()的参数，输出将为一个数字列表
num_list = list(range(1,6))
print(num_list)

print('------')
# 使用函数range()时，还可指定步长。
num_list = list(range(2,11,2))
print(num_list)
num_list = list(range(1,11,2))
print(num_list)

print('------')

# 创建一个列表，其中包含前10个整数（即1~10）的平方
square = []
nums = list(range(1,11))
for num in nums :
    square.append(num ** 2)
print(square)

print('------')