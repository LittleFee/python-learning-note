# 外星人颜色#1：假设在游戏中刚射杀了一个外星人，请创建一个名为
# alien_color 的变量，并将其设置为'green'、'yellow'或'red'。
#  编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出
# 玩家获得了5 个点。
#  编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中
# 未通过（未通过测试时没有输出）。???没看懂，翻译问题？
alien_color='green'
if alien_color=='green':
    print('You got 5 points')
if alien_color != 'green' :
    print('You do not got point')

# 外星人颜色#2：像练习5-3 那样设置外星人的颜色，并编写一个if-else 结构。
#  如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5 个
# 点。
#  如果外星人不是绿色的，就打印一条消息，指出玩家获得了10 个点。
#  编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执
# 行else 代码块。
if alien_color=='green':
    print('You got 5 points')
else:
    print('you got 10 points')

if alien_color!='green':
    print('you got 10 points')
else:
    print('you got 5 points')

# 外星人颜色#3：将练习5-4 中的if-else 结构改为if-elif-else 结构。
#  如果外星人是绿色的，就打印一条消息，指出玩家获得了5 个点。
#  如果外星人是黄色的，就打印一条消息，指出玩家获得了10 个点。
#  如果外星人是红色的，就打印一条消息，指出玩家获得了15 个点。
#  编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条
# 消息。
if alien_color=='green':
    print('you got 5 points')
elif alien_color=='yellow':
    print('you got 10 points')
else:
    print('you got 15 points')

if alien_color=='green':
    print('you got 5 points')

if alien_color=='yellow':
    print('you got 10 points')

if alien_color=='red':
    print('you got 15 points')

# 人生的不同阶段：设置变量age 的值，再编写一个if-elif-else 结构，根据age
# 的值判断处于人生的哪个阶段。
#  如果一个人的年龄小于2 岁，就打印一条消息，指出他是婴儿。
#  如果一个人的年龄为2（含）～4 岁，就打印一条消息，指出他正蹒跚学步。
#  如果一个人的年龄为4（含）～13 岁，就打印一条消息，指出他是儿童。
#  如果一个人的年龄为13（含）～20 岁，就打印一条消息，指出他是青少年。
#  如果一个人的年龄为20（含）～65 岁，就打印一条消息，指出他是成年人。
#  如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。

age=int(input('How old are you ?\n'))
if age<2:
    print('you are a baby')
elif age <4:
    print('you are learning walk')
elif age<13:
    print('you are a children')
elif age<20:
    print('you are a teenager')
elif age <65:
    print('you are a adult')
elif age>=65:
    print('you are old man')


# 喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if
# 语句，检查列表中是否包含特定的水果。
#  将该列表命名为favorite_fruits，并在其中包含三种水果。
#  X 编写5 条if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，
# 就打印一条消息，如“You really like bananas!”。

favorite_fruits=['Bananer','Apple','orange','mango']
if 'Apple' in favorite_fruits:
    print('you are really like apple')
if 'Apple' not in favorite_fruits:
    print('Opps......')