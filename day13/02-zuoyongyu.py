# 有一个名为vars的内置函数，它返回这个不可见的字典
x=2
y=3
dic=vars()
print(dic['x'],dic['y'])
# 2 3
# 一般而言，不应修改vars返回的字典，因为根据Python官方文档的说法，这样做的结果是
# 不确定的。换而言之，可能得不到你想要的结果。

def change_globals():
    global x
    x+=2

print(x)
change_globals()
print(x)


def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor

doulbe=multiplier(5)
print(doulbe(3))# 15
# 在这里，一个函数位于另一个函数中，且外面的函数返回里面的函数。也就是返回一个
# 函数，而不是调用它。重要的是，返回的函数能够访问其定义所在的作用域。换而言之，它
# 携带着自己所在的环境（和相关的局部变量）！
# 每当外部函数被调用时，都将重新定义内部的函数，而变量factor的值也可能不同。由
# 于Python的嵌套作用域，可在内部函数中访问这个来自外部局部作用域（multiplier）的变
# 量，这样存储其所在作用域的函数称为闭包。
# 通常，不能给外部作用域内的变量赋值，但如果一定要这样做，可使用关键字nonlocal。
# 这个关键字的用法与global很像，让你能够给外部作用域（非全局作用域）内的变量赋值。

