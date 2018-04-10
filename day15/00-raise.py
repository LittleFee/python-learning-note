# Python使用异常对象来表示异常状态，并在遇到错误时引发异常。异常对象未被处理（或捕
# 获）时，程序将终止并显示一条错误消息（traceback）。
# raise Exception
# raise Exception('hyperdrive overload')

#
# 创建异常类就像创建其他类一样，但务必直接或间接地继承Exception（这意
# 味着从任何内置异常类派生都可以）自定义异常类的代码类似于下面这样：
class SomeCustomException(Exception):
    pass


