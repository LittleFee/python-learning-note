# 遍历language
languages={
    'Tina':'C',
    'Emily':'C#',
    'Kiwi':'Python',
    }
for key,value in languages.items():
    print('\n'+key+':'+value)
    # print(v)
# 让语句更容易理解，可以改成：
for name,language in languages.items():
    print('\n'+name.title()+':'+language.title())

# 遍历所有的键
# 方法1：
for name in languages.keys():
    print(name.title())
# 方法keys()

# 方法2：
for name in languages:
    print(name)
# 在遍历字典的时候，默认会遍历键，但是使用keys()显式的表达更容易理解


# 打印两条消息，指出两位朋友喜欢的语言。
# 我们像前面一样遍历字典中的名字，但在名字为指定朋友的名字时，打印一条消息，
# 指出其喜欢的语言：
friends=['Kiwi','tina']
for name in languages.keys():
    if name in friends:
        print('Hello '+name+',your language is '+languages[name])
    else:
        print(name+',you are not in the list')

name='kiwi'
if name not in languages.keys():
    print('Come on \n---------------\n')
else:
    print('What ?\n---------------\n')



# 按顺序遍历字典中的所有键
for name in sorted(languages.keys()):
    print(name)
print('\n')
for name in sorted(languages.keys(),reverse=True):
    print(name)
print('\n')

# 遍历字典中的所有值
languages['Liam']='Python'
for language in languages.values():
    print(language)
for language in sorted(languages.values(),reverse=True):
    print(language)

# set 可以去除掉值中的重复值（键本身唯一 所以不需要）
for language in set(languages.values()):
    print(language)