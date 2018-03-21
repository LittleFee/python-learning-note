# Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
# 定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
# 例如一个边长不可变三角形
triangle=(3,4,5)
print(triangle[0])
print(triangle[1])
print(triangle[2])
#试图修改元组内容
# triangle[0]=12
# print(triangle[0])
# File "D:/python-learning-note/day03/0-yuanzu.py", line 9, in <module>
#     triangle[0]=12
# TypeError: 'tuple' object does not support item assignment
for item in triangle :
    print(item)
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。也就是重新定义元组
triangle=(9,16,25)
for item in triangle :
    print(item)
triangle=(1,1)
for item in triangle :
    print(item)