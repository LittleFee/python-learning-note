# 第一个魔术方法就是构造函数（__init__）
class FooBar:
    def __init__(self, value=42):
        self.somevar = value

fb=FooBar()
print(fb.somevar)
# Python提供了魔法方法__del__，也称作析构函数（destructor）。这个方法在对象被销毁
# （作为垃圾被收集）前被调用，但鉴于你无法知道准确的调用时间，建议尽可能不要使
# 用__del__。
