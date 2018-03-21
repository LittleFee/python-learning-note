age = int(input('How old are you ?'))
if age < 10 :
    print('You can do it free')
elif age <= 18 :
    print('You can get a 50 % discount.')
else:
    print('Opps...')

words=['You can do it free','You can get a 50 % discount.','Opps...']
age = int(input('How old are you ?'))
level=0
if age < 10 :
    level=0
elif age <= 18 :
    level=1
else:
    level=2
print(words[level])

# 省略else 代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# 代码块在顾客的年龄超过65（含）时，将价格设置为5美元，这比使用else代码
# 块更清晰些。经过这样的修改后，每个代码块都仅在通过了相应的测试时才会执行。
# else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，
# 这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个elif代码块来
# 代替else代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。