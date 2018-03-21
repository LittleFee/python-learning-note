name_list=['Tom',"petter","Jason","Vivian"]
print(name_list)
print(name_list[1])
print(name_list[1].title())
print(name_list[-1])#倒数第一个 Vivian
print(name_list[-3])#倒数第3个 petter
print('..........')
car=['Audi','BMW','Handa','DasAuto']
print(car[2])
car[2]='Honda'#修改Handa为Honda
print(car[2])

#在列表中添加新元素时，最简单的方式是将元素附加到列表末尾。
# 给列表附加元素时，它将添加到列表末尾。继续使用前一个示例中的列表，在其末尾添加新元素'ducati'
car.append("ducati")
print(car)
#方法append() 将元素'ducati' 添加到了列表末尾，而不影响列表中的其他所有元素：
car1=[]
car1.append(1)
car1.append("DasAuto")
car1.append("34")
print(car1)
print('________________')
# 使用方法insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。
print(car)
car.insert(1,'toyota')
print(car)

#使用del 语句删除元素
del car[2]
print(car)#删除了列表car中的第3个元素‘BMW’

#使用方法pop() 删除元素
# 方法pop() 可删除列表末尾的元素，并让你能够接着使用它。
popedyuansu=car.pop()
print(car)
print(popedyuansu)
#实际上，你可以使用pop() 来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
car2=['Honda','Toyota','Ducati','DasAuto']
print(car2)
second_car=car2.pop(1)
print(car2)
print("我拥有的第二辆车是："+second_car)

# 如果你不确定该使用del 语句还是pop() 方法，下面是一个简单的判断标准：
# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句；
# 如果你要在删除元素后还能继续使用它，就使用方法pop() 。


# 有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove() 。
remove_list=['1',1,'ducati','toyota']
print(remove_list)
# remove_list.remove('1')
remove_list.remove(1)
print(remove_list)