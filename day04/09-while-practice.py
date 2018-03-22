# 7-4 比萨配料：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入
# 'quit'时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添
# 加这种配料。
active=True
while active:
    message=input('add something: ')
    if message=='quit':
        print('End')
        break
    print('add: '+message)

# 7-5 电影票：有家电影院根据观众的年龄收取不同的票价：不到3 岁的观众免费；
# 3~12 岁的观众为10 美元；超过12 岁的观众为15 美元。请编写一个循环，在其中询问
# 用户的年龄，并指出其票价。
active=True
while active:
    age=int(input('How old are you ? '))
    if age <= 0:
        print('End')
        break
    elif age<3:
        print('free')
    elif age<12:
        print('$10')
    elif age>=12:
        print('$15')


# 7-6 三个出口：以另一种方式完成练习7-4 或练习7-5，在程序中采取如下所有做法。
#  在while 循环中使用条件测试来结束循环。
#  使用变量active 来控制循环结束的时机。
#  使用break 语句在用户输入'quit'时退出循环。
print('看上面的代码')


# 7-7 无限循环：编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl +C，
# 也可关闭显示输出的窗口）。
active=True
while active:
    print('I love Shine !')
