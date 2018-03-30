# append
# 方法append用于将一个对象附加到列表末尾。

# 方法clear就地清空列表的内容。
lst = [1, 2, 3]
lst.clear()
print(lst)

# copy
# 这类似于使用a[:]或list(a)，它们也都复制a。
a = [1, 2, 3]
b = a.copy()
b[1] = 4
print(a)

# count
# 方法count计算指定的元素在列表中出现了多少次。
lsts=[1,2,3,4,[1,[2,1]],3,[2,1],1,1,3,4]
print(lsts.count([2,1]))

# extend
# 方法extend让你能够同时将多个值附加到列表末尾
# 用+拼接得到的是一个全新的list
# 用extend会直接改变使用extend的list
a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a)
a.extend(b)
print(a)

# index
# 方法index在列表中查找指定值第一次出现的索引。
number=[0,3,2,1,4,5,6,7,1,2]
print(number.index(1))# 3

# insert
# 方法insert用于将一个对象插入列表。


# pop
# 方法pop从列表中删除一个元素（末尾为最后一个元素），并返回这一元素。
# 注意 pop是唯一既修改列表又返回一个非None值的列表方法。


# push和pop是大家普遍接受的两种栈操作（加入和取走）的名称。Python没有提供push，但可
# 使用append来替代。方法pop和append的效果相反，因此将刚弹出的值压入（或附加）后，得到的
# 栈将与原来相同。

x=[1,2,3,4]
x.append(x.pop())
print(x)

# remove
# 方法remove用于删除第一个为指定值的元素。
# remove是就地修改且不返回值的方法之一。不同于pop的是，它修改列表，但不返
# 回任何值。
lists=['be','c','be']
lists.remove('be')
print(lists)

# reverse
# 方法reverse按相反的顺序排列列表中的元素。
# 注意到reverse修改列表，但不返回任何值（与remove和sort等方法一样）。
lists=[1,2,3,4]
lists.reverse()
print(lists)

# sort
# 方法sort用于对列表就地排序。就地排序意味着对原来的列表进行修改，使其元素按顺序
# 排列，而不是返回排序后的列表的副本。
lists=[1,2,5,7,8,3,6,9]
lists.sort()
print(lists)
lists.sort(reverse=True)
print(lists)

x = [4, 6, 2, 1, 7, 9]
y = x.sort() # Don't do this!
print(y)# none

x=[1,2,7,4,6,5,3]
y=sorted(x,reverse=True)
print(x)
print(y)




