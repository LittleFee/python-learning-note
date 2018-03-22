# 字典的结构是 dictionary{'键名'：'键值','键名'：'键值'}
# 类似于PHP里的关联数组
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 添加键-值对
alien_0['x']=5
alien_0['y']=-1

print(alien_0)

# 使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，
# 通常都需要先定义一个空字典。
dictionary={}
dictionary['item1']='test'

# 修改字典
print('Color of alien is '+alien_0['color'])
alien_0['color']='yellow'
print('Color of alien is '+alien_0['color']+' now')

# 让外星人往右边移动
alien_1={'color':'yellow','speed':'mid','x':12,'y':9}
print('X: '+str(alien_1['x'])+' and y: '+str(alien_1['y']))
speed_now='fast'
if speed_now == 'slow':
    x_inc=1
elif speed_now == 'mid':
    x_inc=3
elif speed_now == 'fast':
    x_inc=5
alien_1['x']=alien_1['x']+x_inc
print('Now x: '+str(alien_1['x'])+' and y: '+str(alien_1['y']))

# 删除字典的键-值对,可以用del来删除
dic_del={'test':1,'tests':2}
print(dic_del)
del dic_del['tests']
print(dic_del)

print('------------------------')
language={
    'tina':'C',
    'emily':'C#',
    'Kiwi':'Python',
    }
print("Kiwi's favorite language is "+
      language['Kiwi']+
      '.'
      )