# 8-9 魔术师： 创建一个包含魔术师名字的列表， 并将其传递给一个名为
# show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
magician_list=['Kiwi','Timo','Kungen','tom']
def show_magicians(lists):
    """打印列表"""
    for name in lists:
        print(name.title())

show_magicians(magician_list)


# 8-10 了不起的魔术师：在你为完成练习8-9 而编写的程序中，编写一个名为
# make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the
# Great”。调用函数show_magicians()，确认魔术师列表确实变了。
def make_great(lists):
    """给列表中每个元素都加上the Great"""
    index=0
    for name in lists:
        lists[index]='the Great '+name
        index+=1

make_great(magician_list)
show_magicians(magician_list)


# 8-11 不变的魔术师：修改你为完成练习8-10 而编写的程序，在调用函数
# make_great()时，向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后
# 的列表，并将其存储到另一个列表中。分别使用这两个列表来调用show_magicians()，
# 确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样“the
# Great”的魔术师名字。

def make_great2(lists):
    """获得一个新的列表"""
    num=0
    for name in lists:
        lists[num]='the Great '+name
        num+=1
    return  lists

great_magicians=make_great2(magician_list[:])

show_magicians(magician_list)
show_magicians(great_magicians)
