# 字典中的键可以是任何不可变的类型，如浮点数（实数）、字符串或元组。


# 表达式k in d（其中d是一个字典）查找的是键而不是值
dicts={'kiwi':123,345:'kiwi'}
print('kiwi' in dicts)
print(123 in dicts)

database={
    'Kiwi':{
        'addr':'sichuan',
        'age':25
    },
    'shine':{
        'addr':'nanchong',
        'age':24
    }
}
print(database['Kiwi']['age'])
for k,v in database.items():
    print(k+':')
    for key,val in v.items():
        print('-'+key+':'+str(val))
string='Kiwi\'s phone is {Kiwi}'
phone={'Kiwi':'1387264','Shine':'887799'}
print(string.format_map(phone))