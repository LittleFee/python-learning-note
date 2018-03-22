# 6-1 人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
# 该字典应包含键first_name、last_name、age 和city。将存储在该字典中的每项信息都
# 打印出来。
person={
    'first_name':'Kiwi',
    'last_name':'qing',
    'age':25,
    'city':'Chengdu',
    }
print('First name：'+person['first_name'])
print('Last name: '+person['last_name'])
print('Age: '+str(person['age']))
print('City: '+person['city'])

print('------1-----')

# 6-2 喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出5 个人的名字，
# 并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存储
# 在字典中。打印每个人的名字和喜欢的数字。
favorite_num={
    'Kiwi':7,
    'Shine':3,
    'Liam':2,
    'Emily':1,
    'Tina':9,
    }
favorite="'s favorite number is "
print('Kiwi'+favorite+str(favorite_num['Kiwi']))
print('Shine'+favorite+str(favorite_num['Shine']))
print('Liam'+favorite+str(favorite_num['Liam']))
print('Emily'+favorite+str(favorite_num['Emily']))
print('Tina'+favorite+str(favorite_num['Tina']))

print('------2-----')

# 6-3 词汇表：Python 字典可用于模拟现实生活中的字典，但为避免混淆，我们将后
# 者称为词汇表。
#  想出你在前面学过的5 个编程词汇，将它们用作词汇表中的键，并将它们的含
# 义作为值存储在词汇表中。
#  以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加
# 上一个冒号，再打印词汇的含义；也可在一行打印词汇，再使用换行符（\n）
# 插入一个空行，然后在下一行以缩进的方式打印词汇的含义。
cihuibiao={
    'PHP':'超文本预处理器',
    'range':'用于生成指定范围内的数字的函数',
    'if':'条件判断语句',
    '元组':'不可变的列表',
    '字典':'类似php里的数组'
    }
print('PHP：\n\t'+cihuibiao['PHP'])
print('range：\n\t'+cihuibiao['range'])
print('if：\n\t'+cihuibiao['if'])
print('元组：\n\t'+cihuibiao['元组'])
print('字典：\n\t'+cihuibiao['字典'])