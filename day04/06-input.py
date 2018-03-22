# 函数input()的工作原理
message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# 通过在提示末尾（这里是冒号后面）包含一个空格，可将提示与用户输入分开，让用户清楚
# 地知道其输入始于何处
name=input('Could you tell me your name?: ')
print('OK,'+name+' I know your name now')


# 使用int()来获取数值输入
age=input('How old are you ? : ')
age=int(age)
if age >= 18:
    print('You are not a baby now old man!')
else:
    print('You are not a man little boy ~')


# 求模运算符 %
print(4%3)

# 如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0。你可利用这一点来判
# 断一个数是奇数还是偶数
number=int(input("告诉我一个数字，我会告诉你它是奇数还是偶数"))
if number % 2 == 0:
    print('你输入的'+str(number)+'是一个偶数')
else:
    print('你输入的'+str(number)+'是一个奇数')


# Python 2.7也包含函数input()，但它将用户输入解读为Python代码，并尝试运行它们。因此，
# 最好的结果是出现错误，指出Python不明白输入的代码；而最糟的结果是，将运行你原本无意运
# 行的代码。如果你使用的是Python 2.7，请使用raw_input()而不是input()来获取输入。
