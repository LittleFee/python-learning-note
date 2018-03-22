# while 循环简介
# for循环用于针对集合中的每个元素都一个代码块，而while循环不断地运行，直到指定的条
# 件不满足为止
number=int(input('来免费叫哥哥的时候到了，想让我叫你多少声哥哥： '))
if number < 0:
    number=1
count=0
while count<number:
    print('小哥哥')
    count+=1


# 让用户选择何时退出
lists=[]
message='来告诉我你想去哪里耍，说完了的话就输个quit，来嘛： '
place=""
while place.lower() != 'quit':
    place = input(message)
    if place.lower() != 'quit':
        lists.append(place)
print("你想去的地方有这些：")
for item in lists:
    print('\t'+item)


# 使用标志
# 这样做的好处显而易见，即使有多种情况可以结束循环，我们也只需要在循环体了进行
# 条件判断，随时可以结束循环，而之前的程序只限制在用户输入了'quit'
lists=[]
message='来告诉我你想去哪里耍，说完了的话就输个quit，来嘛： '
place=""
active=True
while active:
    place = input(message)
    if place.lower() != 'quit':
        lists.append(place)
    else:
        active=False
print("你想去的地方有这些：")
for item in lists:
    print('\t'+item)


# 要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用
# break语句
lists = []
message = '来告诉我你想去哪里耍，说完了的话就输个quit，来嘛： '
place = ""
active = True
while active:
    place = input(message)
    if place.lower() != 'quit':
        lists.append(place)
    else:
        break
print("你想去的地方有这些：")
for item in lists:
    print('\t' + item)


# 在循环中使用continue
# 例如让程序只打印0-100中的偶数
number=0
while number <= 100:
    number+=1
    if number % 2 != 0:
        continue
    print(number)