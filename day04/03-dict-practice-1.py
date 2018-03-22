# 6-4 词汇表2：既然你知道了如何遍历字典，现在请整理你为完成练习6-3 而编写
# 的代码，将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。确定
# 该循环正确无误后，再在词汇表中添加5 个Python 术语。当你再次运行这个程序
# 时，这些新术语及其含义将自动包含在输出中。
cihuibiao={
    'PHP':'超文本预处理器',
    'range':'用于生成指定范围内的数字的函数',
    'if':'条件判断语句',
    '元组':'不可变的列表',
    '字典':'类似php里的数组',
    '迭代':'遍历',
    '遍历':'迭代',
    '布尔表达式':'True or False',
    '切片':'部分使用列表lists[2:5]，第三个到第四个',
    }
for name,meaning in cihuibiao.items():
    print(name+':\n\t'+meaning)


# 6-5 河流：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—
# 值对可能是'nile': 'egypt'。
#  使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
#  使用循环将该字典中每条河流的名字都打印出来。
#  使用循环将该字典包含的每个国家的名字都打印出来。
rivers={'nile':'egypt','changjiang river':'china','lanchang river':'india'}
for river,country in rivers.items():
    print('The '+river.title()+' runs through '+country.title()+'.\n')

for river in rivers.keys():
    print(river.title()+'\n')

for country in rivers.values():
    print(country.title()+'\n')


# 6-6 调查：在6.3.1 节编写的程序favorite_languages.py 中执行以下操作。
#  创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人
# 未包含在字典中。
#  遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未
# 参与调查的人，打印一条消息邀请他参与调查。
languages={
    'Tina':'C',
    'Emily':'C#',
    'Kiwi':'Python',
    }
namelist=['Tina','liam','bob']
for name in namelist:
    if name in languages.keys():
        print('Thx '+name.title())
    else:
        print('I invite you,'+name)