# 传递列表
# 需求：一堆要打印的东西，打印完成以后，存储到打印完成列表，最后返回打印完成列表
# 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永
# 久性的，这让你能够高效地处理大量的数据。

unprint=['excel','word','ppt','pdf']
printed=[]
def do_print(un):
    """打印并把元素存入新表"""
    while un:
        cprint=un.pop()
        print(cprint)
        printed.append(cprint)

do_print(unprint)
print(printed)
print(unprint)

# 禁止函数修改列表
# 在上述函数中我们在打印完了之后原来的列表就会被修改了（传值和传引用），
# 要想原list 不被修改，请使用切片（也就是传递一个副本）来处理，如下：
unprint2=['excel','word','ppt','pdf']

do_print(unprint2[:])
print(printed)
print(unprint2)