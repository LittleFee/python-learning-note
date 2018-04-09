# 函数exec将字符串作为代码执行。
# exec('print(\'hello\')')
# hello
# 调用函数exec时只给它提供一个参数绝非好事。在大多数情况下，还应向它传递一个
# 命名空间——用于放置变量的地方；否则代码将污染你的命名空间，即修改你的变量。例如，假
# 设代码使用了名称sqrt，结果将如何呢？
# >>> from math import sqrt
# >>> exec("sqrt = 1")
# >>> sqrt(4)
# Traceback (most recent call last):
#  File "<pyshell#18>", line 1, in ?
#  sqrt(4)
# TypeError: object is not callable: 1
# 既然如此，为何要将字符串作为代码执行呢？函数exec主要用于动态地创建代码字符串。如
# 果这种字符串来自其他地方（可能是用户），就几乎无法确定它将包含什么内容。因此为了安全
# 起见，要提供一个字典以充当命名空间。
from math import sqrt
scope = {}
exec("sqrt = 1",scope)
print(sqrt(4))
