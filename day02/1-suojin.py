magicians=['tom','larry','jim','timor']
print('The name list of magicians:')
for magician in magicians:
print('\t'+magician.title())
print('\tGreat!')
#
# 以上代码会报如下错：
# File "D:/PythonLearning/day02/2-suojin.py", line 4
#     print('\t'+magician.title()+',we are looking forward your next show')
#         ^
# IndentationError: expected an indented block
# 通常，将紧跟在for语句后面的代码行缩进，可消除这种缩进错误。

magicians=['tom','larry','jim','timor']
print('The name list of magicians:')
for magician in magicians:
    print('\t'+magician.title()+',we are looking forward your next show')
print('\tGreat!')
#
# 以上代码不会报错，但是原本个魔术师都应当得到一个great！，但是由于第二个print没有缩进，
# 因此只有等待for循环完成后才打印。

message = "清渭技术小站：https://www.qingwei.tech"
    print(message)
#
# 以上代码是典型的不应该缩进的时候缩进，因为第二句并不属于第一句，此时Python会报错
# 为避免意外缩进错误，请只缩进需要缩进的代码。在前面编写的程序中，只有要在for循环中对每个元
# 素执行的代码需要缩进。

