# 4-10 切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
#  打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个
# 元素。
#  打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中
# 间的三个元素。
#  打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三
# 个元素。
players=['lindan','malong','lizongwei','chenglong','guojinjin']
print('The first three items in the list are:')
for player in players[:3] :
    print(player.title())
print('Three items from the middle of the list are:')
for player in players[1:-1] :
    print(player.title())

print('The last three items in the list are:')
for player in players[-3:] :
    print(player.title())


# 你的比萨和我的比萨：在你为完成练习4-1 而编写的程序中，创建比萨列表的
# 副本，并将其存储到变量friend_pizzas 中，再完成如下任务。
#  在原来的比萨列表中添加一种比萨。
#  在列表friend_pizzas 中添加另一种比萨。
#  核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一
# 个for 循环来打印第一个列表；打印消息“My friend’s favorite pizzas are:”，再使
# 用一个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
my_pizzas=['beef','poke','chicken','fish','fruits']
friend_pizzas=my_pizzas[:]
my_pizzas.append('rice')
friend_pizzas.append('mango')
print('My favorite pizzas are:')
for pizza in my_pizzas :
    print(pizza)
print('My friend’s favorite pizzas are:')
for pizza in friend_pizzas :
    print(pizza)

# 4-12 使用多个循环：在本节中，为节省篇幅，程序foods.py 的每个版本都没有使用
# for 循环来打印列表。请选择一个版本的foods.py，在其中编写两个for 循环，将各个
# 食品列表都打印出来。
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
# print(my_foods)
for food in my_foods :
    print(food)

print("\nMy friend's favorite foods are:")
# print(friend_foods)
for food in friend_foods :
    print(food)