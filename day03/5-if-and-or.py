# 检查多个条件
# 你可能想同时检查多个条件，例如，有时候你需要在两个条件都为True时才执行相应的操作，
# 而有时候你只要求一个条件为True时就执行相应的操作。在这些情况下，关键字and和or可助你
# 一臂之力。

# and
number=input('give me a number : ')
if (int(number)>=12) and (int(number)<=17):
    print('In the range')
else :
    print('try again')

# or
number=input('Please give me a number')
if (int(number)>100) or (int(number)<22):
    print('In the range')
else :
    print('Out of range')