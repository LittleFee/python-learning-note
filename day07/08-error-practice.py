# 10-6 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是
# 文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发TypeError 异
# 常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的
# 任何一个值不是数字时都捕获TypeError 异常，并打印一条友好的错误消息。对你编写
# 的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
while True:
    print('给我两个数，我给你它们的和（输入n停止运算）')
    num_1 = input('第一个数： ')
    if num_1.lower() == 'n':
        break
    num_2 = input('第二个数： ')
    if num_2.lower() == 'n':
        break
    try:
        ans = float(num_1) + float(num_2)
    except ValueError:
        print('加法是算数的哦，请重新输入')
    else:
        print(num_1+'+'+num_2+'='+str(ans))

# 10-7 加法计算器：将你为完成练习10-6 而编写的代码放在一个while 循环中，让
# 用户犯错（输入的是文本而不是数字）后能够继续输入数字。
# ---见上面代码

# 10-8 猫和狗：创建两个文件cats.txt 和dogs.txt，在第一个文件中至少存储三只猫的
# 名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并
# 将其内容打印到屏幕上。将这些代码放在一个try-except 代码块中，以便在文件不存
# 在时捕获FileNotFound 错误，并打印一条友好的消息。将其中一个文件移到另一个地方，
# 并确认except 代码块中的代码将正确地执行。
def file_read(file_name):
    """读取并打印文件内容"""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('Sorry,the file ' + file_name + '  doesn\'t exist!')
        # pass
    else:
        print(contents)
file_list=['cats.txt','dogs.txt','babys.txt']
for file in file_list:
    file_read(file)
# 10-9 沉默的猫和狗：修改你在练习10-8 中编写的except 代码块，让程序在文件不
# 存在时一言不发。
# 上题代码把print('Sorry,the file ' + file_name + '  doesn\'t exist!')注释了就OK

# 10-10 常见单词：访问项目Gutenberg（http://gutenberg.org/），并找一些你想分析的
# 图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 你可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。例如，
# 下面的代码计算'row'在一个字符串中出现了多少次：
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# 请注意，通过使用lower()将字符串转换为小写，可捕捉要查找的单词出现的所有
# 次数，而不管其大小写格式如何。
# 编写一个程序，它读取你在项目Gutenberg 中获取的文件，并计算单词'the'在每
# 个文件中分别出现了多少次。
def count_words(file_name,word):
    """统计文件中有多少个特定单词"""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('Sorry,the file ' + file_name + '  doesn\'t exist!')
    else:
        num = contents.lower().count(word)
        print(file_name + ' 中有 ' + str(num) + ' 个'+word)

count_words('alice.txt','the')
