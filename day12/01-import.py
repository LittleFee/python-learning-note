# 可同时（并行）给多个变量赋值
x,y,z = 1,2,3
print(x,y,z)
# 1 2 3
x,y = y,x
print(x,y,z)
# 2 1 3

# 这里执行的操作称为序列解包（或可迭代对象解包）：将一个序列（或任何可迭代
# 对象）解包，并将得到的值存储到一系列变量中。
values=1,2,3,4,5
print(values)
# (1, 2, 3, 4, 5)
x,y,z,a,b=values
print(a,b,x,y,z)
# 4 5 1 2 3

# 这在使用返回元组（或其他序列或可迭代对象）的函数或方法时很有用。假设要从字典中随
# 便获取（或删除）一个键-值对，可使用方法popitem，它随便获取一个键值对并以元组的方式
# 返回。接下来，可直接将返回的元组解包到两个变量中。
a = {'Kiwi':26,'Shine':25,'Bye':23}
tryit = a.popitem()
print(tryit)
# ('Bye', 23)
key,value = tryit
print(key,value)
# Bye 23

# 可使用星号运算符（*）来收集多余的值，这样无需确保值和变量的个数相同
a, b, *rest = [1, 2, 3, 4]
print(a)# 1
print(b)# 2
print(rest)# [3'4]
# 还可将带星号的变量放在其他位置。
name = "I love FYX and python"
first, *middle, last = name.split()
print(first,last)
# I python
print(middle)
# ['love FYX and', 'FYX ', 'and']
# 赋值语句的右边可以是任何类型的序列，但带星号的变量最终包含的总是一个列表。在变量
# 和值的个数相同时亦如此。
a, *b, c = "abc"
print(a, b, c )
# a ['b'] c

# 链式赋值

x = y = 23
print(x)# 23
print(y)# 23
y = 32
print(x)# 23
print(y)# 32
# 改变链式赋值的其中一个值别的值不会改变

