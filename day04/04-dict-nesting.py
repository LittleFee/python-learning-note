# 如何在一个列表里嵌套很多个外星人的信息？
# 字典列表
alien_0={'color':'green','x':5,'y':4}
alien_1={'color':'red','x':3,'y':-1}
alien_2={'color':'yellow','x':-12,'y':5}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)


# 自动创建三个属性相同的外星人
new_aliens=[]
for alen_num in range(0,30):# 1,31
    new_aliens.append({'color':'red','x':2,'y':alen_num})
for alien in new_aliens[0:5]:
    print(alien)
for alien in new_aliens[0:3]:
    if alien['color']=='red':
        alien['color']='yellow'
        alien['x']+=3
for alien in new_aliens[0:3]:
    print(alien)

# 在字典中存储列表
# 例如，你如何描述顾客点的pizza呢
pizza={
    'name':'kiwi',
    'peiliao':['土豆','牛肉','小番茄']
    }
print(pizza['name']+',你预定了一个汉堡，他有如下配料：\n')
for peiliao in pizza['peiliao']:
    print('\t'+peiliao)

f_language={
    'Kiwi':['python','php','vue'],
    'Tina':['html','vue'],
    'Emily':['js','java','jsp','c#'],
    'Stanley':['english']
}
for name,lang in f_language.items():
    if len(lang)>1:
        print(name+' loves these languages are:')
    else:
        print(name + ' loves language is:')

    for item in lang:
        print('\t'+item)

    print('\n')

# 在字典中存储字典
users={
   '0001':{
       'name':'Kiwi',
       'age':25,
       'sex':'male'
       },
   '0002':{
       'name':'Tina',
       'age':30,
       'sex':'female'
       } ,
   '0003':{'name':'Liam','age':31,'sex':'male'}
}
for code,profile in users.items():
    print('编号: '+code+' 的个人资料如下：')

    for item,detail in profile.items():
        print('\t'+item+' : '+str(detail))

    print('\n')