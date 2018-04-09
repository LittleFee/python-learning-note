# # 并行迭代
name=['kiwi','tina','shine','liam']
age=['25','36','24','30']
# for name,age in zip(name,age):
#     print(name+"'s name is "+str(age))

# 置函数zip，它将两个序列“缝合”起来，并返回一个由元组组成的序列。
# 返回值是一个适合迭代的对象，要查看其内容，可使用list将其转换为列表。
z=list(zip(name,age))
print(z)

# 函数zip可用于“缝合”任意数量的序列。需要指出的是，当序列的长度不同时，函数zip将
# 在最短的序列用完后停止“缝合”。
a=list(zip(range(5), range(100000000)))
print(a)


# 内置函数enumerate让你能够迭代索引-值对，其中的索引是自动提供的。
# strings='jjfhfhfhfdx'
# for index, string in enumerate(strings):
#     if 'x' in string:
#         strings[index] = '[censored]'

# pass什么都不做
# exec

