# 1.数到20：使用一个for 循环打印数字1~20（含）
for num in range(1,21) :
    print(num)
print('------End 1------')

# 2.一百万：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这
# 些数字打印出来（如果输出的时间太长，按Ctrl + C 停止输出，或关闭输出窗口）。
for num in range(1,1000001) :
    print(num)
print('------End 2------')

# 3.计算1~1 000 000 的总和：创建一个列表，其中包含数字1~1 000 000，再使用
# min()和max()核实该列表确实是从1 开始，到1 000 000 结束的。另外，对这个列表调
# 用函数sum()，看看Python 将一百万个数字相加需要多长时间。
nums = list(range(1,1000001))
print('min:'+str(min(nums)))
print('max:'+str(max(nums)))
print('sum:'+str(sum(nums)))

print('------End 3------')

# 4.奇数：通过给函数range()指定第三个参数来创建一个列表，其中包含1~20 的奇数；
# 再使用一个for 循环将这些数字都打印出来。
odds=list(range(1,21,2))
for odd in odds :
    print(odd)
print('------End 4------')

# 5. 3 的倍数：创建一个列表，其中包含3~30 内能被3 整除的数字；
# 再使用一个for循环将这个列表中的数字都打印出来。
list_3=list(range(3,31,3))
for num in list_3 :
    print(num)
# for num in range(3,31,3) :
#     print(num)
print('------End 5------')

# 6.立方：将同一个数字乘三次称为立方。例如，在Python 中，2 的立方用2**3表示。
# 请创建一个列表，其中包含前10 个整数（即1~10）的立方，
# 再使用一个for 循环将这些立方数都打印出来。
# cubes=[num ** 3 for num in range(1,11)]
cubes=[]
nums=list(range(1,11))
for num in nums :
    cubes.append(num ** 3)

for cube in cubes :
    print(cube)

print('------End 6------')

# 7.立方解析：使用列表解析生成一个列表，其中包含前10 个整数的立方。
cubes=[num ** 3 for num in range(1,11)]
print(cubes)