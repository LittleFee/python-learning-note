# Python方法sort() 让你能够较为轻松地对列表进行排序
# 值得注意的是sort对列表的排序是永久性的
car=['toyota','honda','bmw','ducati']
print(car)
car.sort()
print(car)

print('===========================')
# 如果给sort一个reverse=True的参数，则按照字母顺序倒序排列
car.sort(reverse=True)
print(car)

print('===========================')


# 要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted() 。
# 函数sorted() 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。
car=['toyota','honda','bmw','ducati']
print("This is new list order:\n")
print(sorted(car))
print("this is origin list:\n")
print(car)
# 如果你要按与字母顺序相反的顺序显示列表，也可向函数sorted() 传递参数reverse=True
print("this is reverse list:\n")
print(sorted(car,reverse=True))
print(car)

print('===========================')

# 要反转列表元素的排列顺序，可使用方法reverse() 。
# 注意，reverse() 不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序
print('Origin:\n')
print(car)
print('After reverse()\n')
car.reverse()
print(car)

# 方法reverse() 永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse() 即可。
print('==========================')