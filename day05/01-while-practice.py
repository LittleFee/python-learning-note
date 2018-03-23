# 7-8 熟食店：创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名
# 字；再创建一个名为finished_sandwiches 的空列表。遍历列表sandwich_orders，对于
# 其中的每种三明治，都打印一条消息，如I made your tuna sandwich，并将其移到列表
# finished_sandwiches。所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders=['Big Mac','Filet-o-Fish','McChicken','Chicken McNuggets']
finished_sandwiches=[]
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print('I made your '+current_sandwich)
    finished_sandwiches.append(current_sandwich)
# print(sandwich_orders) # 检查是否全部转移完成
for sandwich in finished_sandwiches:
    print(sandwich)


# 7-9 五香烟熏牛肉（pastrami）卖完了：使用为完成练习7-8 而创建的列表
# sandwich_orders，并确保'pastrami'在其中至少出现了三次。在程序开头附近添加这样
# 的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个while 循环将
# 列表sandwich_orders 中的'pastrami'都删除。确认最终的列表finished_sandwiches 中
# 不包含'pastrami'。
sandwich_orders=[
    'Big Mac',
    'pastrami',
    'Filet-o-Fish',
    'McChicken',
    'pastrami',
    'Chicken McNuggets',
    'pastrami',

    ]
finished_sandwiches=[]
print(sandwich_orders)
print('Pastrami has been sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print('I made your '+current_sandwich)
    finished_sandwiches.append(current_sandwich)
print(sandwich_orders)
for sandwich in finished_sandwiches:
    print(sandwich)


# 7-10 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“If
# you could visit one place in the world, where would you go?”的提示，
#  并编写一个打印调查结果的代码块。
research={}
active=True
while active:
    name=input('What\' your name ? ')
    ans=input('If you could visit one place in the world, where would you go?')
    research[name]=ans
    quit=input('Any else ?(yes/no)')
    if quit=='no':
        active=False
for name,ans in research.items():
    print(name+':'+ans)