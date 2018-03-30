# 给切片赋值
lists=list('Perl')
lists[1:]='ython'
print(lists)
lists[1:3]=[]# 等同于lists[1:3]
print(lists)
# 使用切片赋值还可在不替换原有元素的情况下插入新元素。
number=[1,5]
number[1:1]=[2,3,4]
print(number)