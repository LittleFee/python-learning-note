# 6-7 人：在为完成练习6-1 而编写的程序中，再创建两个表示人的字典，然后将这
# 三个字典都存储在一个名为people 的列表中。遍历这个列表，将其中每个人的所有信
# 息都打印出来。
kiwi={
    'first_name':'Kiwi',
    'last_name':'qing',
    'age':25,
    'city':'Chengdu',
    }
tina={
    'first_name':'Tina',
    'last_name':'wang',
    'age':26,
    'city':'Chengdu',
    }
liam={
    'first_name':'liam',
    'last_name':'li',
    'age':26,
    'city':'Chengdu',
    }
persons=[kiwi,tina,liam]
for person in persons:
    for item,detail in person.items():
        print(item+' : '+str(detail))
    print('\n')


# 6-8 宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在
# 每个字典中，包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets 的列
# 表中，再遍历该列表，并将宠物的所有信息都打印出来。
doufu={'type':'cat','boss':'kiwi'}
mangzi={'type':'dog','boss':'mige'}
wugui={'type':'turtle','boss':'jiage'}
pets=[doufu,mangzi,wugui]
for pet in pets:
    for type,boss in pet.items():
        print(type+':'+boss)

    print('\n')


# 6-9 喜欢的地方：创建一个名为favorite_places 的字典。在这个字典中，将三个
# 人的名字用作键；对于其中的每个人，都存储他喜欢的1~3 个地方。为让这个练习更有
# 趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字
# 及其喜欢的地方打印出来。
favorite_places={
    'Kiwi':['Finland','Japan','China'],
    'Shine':['Japan','France','Italy'],
    'Sunny':['Vietnam','Thailand'],
    'Dingding':['Japan'],
    }
for name,places in favorite_places.items():
    if len(places)>1:
        print(name+' likes these places: ')
    else:
        print(name+' likes this place: ')
    for place in places:
        print(place)
    print('\n')


# 6-10 喜欢的数字：修改为完成练习6-2 而编写的程序，让每个人都可以有多个喜欢
# 的数字，然后将每个人的名字及其喜欢的数字打印出来。
favorite_num={
    'Kiwi':[1,7],
    'Shine':[2,5],
    'Liam':[3,7,6],
    'Emily':[2,4,5,6,7],
    'Tina':[9],
    }
for name,nums in favorite_num.items():
    if len(nums)>1:
        print(name+' likes these numbers:')
    else:
        print(name+' likes this number:')
    for num in nums:
        print(num)
    print('\n')



# 6-11 城市：创建一个名为cities 的字典，其中将三个城市名用作键；对于每座城
# 市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市
# 的事实。在表示每座城市的字典中，应包含country、population 和fact 等键。将每座
# 城市的名字以及有关它们的信息都打印出来。
cities={
    'Mianyang':{
        'country':'china',
        'population':13,
        'fact':'mifen is really delicious',
        },
    'Tokoyo':{
        'country':'japan',
        'population':1,
        'fact':'AV is so hot',
        },
    'newyork':{
        'country':'USA',
        'population':3,
        'fact':'I like Tesla',
        },
}
for name,details in cities.items():
    print('These are some information of '+name.title()+':')
    for item,detail in details.items():
        print('\t'+item.title()+' : '+str(detail))
    print('\n')


# 打印所有城市的名字（打印字典的键）
# 如果要打印字典的值，就用 dictionar.values()

for name in cities.keys():
    print(name.title())

# 删除绵阳的信息
del cities['Mianyang']
for name in cities.keys():
    print(name.title())