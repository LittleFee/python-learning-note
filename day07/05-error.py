# 处理ZeroDivisionError 异常
# 把一个数字除以0的时候就会出现这个错误
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

