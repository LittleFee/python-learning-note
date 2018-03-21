cars=['toyota','bmw','honda','audi']
for car in cars :
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

# Python 大小写敏感
word='WORD'
if word=='word':
    print('True')
else:
    print('False')

# 可以用.lower()来
if word.lower()=='word':
    print('True')
else:
    print('False')

# 不相等 用 !
word='word'
if word!='word':
    print('!Equal')
else:
    print('Equal')