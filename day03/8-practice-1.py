# 条件测试：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结
# 果都打印出来。你编写的代码应类似于下面这样：
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
#  详细研究实际结果，直到你明白了它为何为True 或False。
#  创建至少10 个测试，且其中结果分别为True 和False 的测试都至少有5 个。
baby='FYX'
print("baby is FYX ? I think so!")
print(baby=='FYX')
print("baby is QW ? I think not!")
print(baby=='QW')

cars=['toyota','honda','volvo','benz']

print('I think benz is in the list')
if 'benz' in cars :
    print('True')

print('I think lotus is not in the list')
if 'lotus' not in cars :
    print('True')

print('I think benz and volvo both in the list')
if ('benz' in cars) and ('volvo' in cars) :
    print('True')

print('I think benz or lotus in the list')
if ('benz' in cars) or ('lotus' in cars) :
    print('True')

number=input('Input a number plz')
if int(number) > 0 :
    print('True')
else:
    print('False')