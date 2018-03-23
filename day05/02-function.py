# 定义函数
# 例子 定义一个简单的打招呼的函数
def say_hello():
    """简单打招呼的函数"""
    print('Hello Python')

say_hello()

# 改进版，可以给名字打印
def say_hello_1(username):
    print('Hello '+username.title())

say_hello_1('kiwi')

# 在函数say_hello_1()的定义中，变量username是一个形参(parameter)——函数完成其工作所需的一项信
# 息。在代码say_hello_1('kiwi')中，值'kiwi'是一个实参(arguments)。实参是调用函数时传递给函数的信
# 息。我们调用函数时，将要让函数使用的信息放在括号内。在say_hello_1('kiwi')中，将实参
# 'kiwi'传递给了函数say_hello_1()，这个值被存储在形参username中。