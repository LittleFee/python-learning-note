# 在列表之间移动元素
new_users=['alice','tom','lisa','lemon']
comfirmed_users=[]
while new_users:
    add_user=new_users.pop()
    print('Added '+add_user.title()+' to list')
    comfirmed_users.append(add_user)

for item in comfirmed_users:
    print(item)

# 删除列表中多个重复的值
# 例如删除下面animals中的cat,如果要全部删除很不容易，这里可以用while
animals=['cat','dog','chicken','cat','bird','cat','fish']
print(animals)
animals.remove('cat')
print(animals)
while 'cat' in animals:
    animals.remove('cat')

print(animals)


# 使用用户输入来填充字典
# 例如，模拟一个简单的用户调查
active=True
responses={}
while active:
    name=input('What\'your name: ')
    age=int(input('How old are you ?'))
    status=input('Anyone else ?(yes/no)')
    responses[name]=age
    if status.lower()=='no':
        active=False

for name,age in responses.items():
    print('name:'+name)
    print('age:'+str(age))

