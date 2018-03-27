# 10-1 Python 学习笔记：在文本编辑器中新建一个文件，写几句话来总结一下你至
# 此学到的Python 知识，其中每一行都以“In Python you can”打头。将这个文件命名为
# learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。编写一
# 个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个文件；
# 第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在with 代码
# 块外打印它们。
file_name='learning_python.txt'
with open(file_name) as file_object:
    python_string=file_object.read()
    print(python_string)

with open(file_name) as file_object:
    for line in file_object:
        print(line)

with open(file_name) as file_object:
    file_list=file_object.readlines()
for item in file_list:
    print(item)
print(file_list)

# 10-2 C 语言学习笔记：可使用方法replace()将字符串中的特定单词都替换为另一
# 个单词。下面是一个简单的示例，演示了如何将句子中的'dog'替换为'cat'：
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# 读取你刚创建的文件learning_python.txt 中的每一行，将其中的Python 都替换为另
# 一门语言的名称，如C。将修改后的各行都打印到屏幕上。
with open(file_name) as file_object:
    list=file_object.readlines()
for line in list:
    print(line.replace('Python','PHP'))