# 9-14 骰子：模块random 包含以各种方式生成随机数的函数，其中的randint()返回
# 一个位于指定范围内的整数，例如，下面的代码返回一个1~6 内的整数：
# from random import randint
# x = randint(1, 6)
# 请创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。编写一
# 个名为roll_die()的方法，它打印位于1 和骰子面数之间的随机数。创建一个6 面的骰
# 子，再掷10 次。
# 创建一个10 面的骰子和一个20 面的骰子，并将它们都掷10 次
from random import randint

class Die():
    """die 类"""
    def __init__(self):
        """初始化"""
        self.sides=6

    def roll_die(self):
        """生成并打印相应数字"""
        num = randint(1, self.sides+1)
        for num in range(1,num):
            print(num)
        print('------')

roll=Die()
roll.sides=6
for i in range(0,10):
    roll.roll_die()
roll.sides=10
for i in range(0,10):
    roll.roll_die()
roll.sides=20
for i in range(0,10):
    roll.roll_die()