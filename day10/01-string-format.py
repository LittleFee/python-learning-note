from math import pi,ceil

# 替换字段名

# 向format提供要设置其格式的未命名参数，并在格式字符串中使用
# 未命名字段。此时，将按顺序将字段和参数配对。
strings='{} love {} fyx'
print(strings.format('I','you'))

# 还可通过索引来指定要在哪个字段中使用相应的未命名参数，这样可不按顺序使用未命名
# 参数。

str="{name} is approximately {value}.Do {0} like {1}"
print(str.format('you','it',value=pi, name="π",) )

# 指定要在字段中包含的值后，就可添加有关如何设置其格式的指令了。首先，可以提供一个
# 转换标志
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))

# 上述三个标志（s、r和a）指定分别使用str、repr和ascii进行转换。函数str通常创建外观
# 普通的字符串版本（这里没有对输入字符串做任何处理）。函数repr尝试创建给定值的Python表
# 示（这里是一个字符串字面量）。函数ascii创建只包含ASCII字符的表示，类似于Python 2中的
# repr。

# 你还可指定要转换的值是哪种类型，更准确地说，是要将其视为哪种类型。例如，你可能提
# 供一个整数，但将其作为小数进行处理。为此可在格式说明（即冒号后面）使用字符f（表示定
# 点数）。
print("The number is {num}".format(num=42))
# The number is 42
print("The number is {num:f}".format(num=42))
# The number is 42.000000
print("The number is {num:.3f}".format(num=42))
# The number is 42.000

# b 将整数表示为二进制数
# c 将整数解读为Unicode码点
# d 将整数视为十进制数进行处理，这是整数默认使用的说明符
# e 使用科学表示法来表示小数（用e来表示指数）
# E 与e相同，但使用E来表示指数
# f 将小数表示为定点数
# F 与f相同，但对于特殊值（nan和inf），使用大写表示
# g 自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数
# G 与g相同，但使用大写来表示指数和特殊值
# n 与g相同，但插入随区域而异的数字分隔符
# o 将整数表示为八进制数
# s 保持字符串的格式不变，这是默认用于字符串的说明符
# x 将整数表示为十六进制数并使用小写字母
# X 与x相同，但使用大写字母
# % 将数表示为百分比值（乘以100，按说明符f设置格式，再在后面加上%）

# 宽度、精度
print("{num:10}".format(num=3) )
#          3
print("{pi:10.2f}".format(pi=pi) )
#       3.14

# 千位分隔符
print('Our nation have about {number:,} people'.format(number=100**4*14))

# 符号、对齐和用 0 填充
# 有很多用于设置数字格式的机制，比如便于打印整齐的表格。在大多数情况下，只需指定宽
# 度和精度，但包含负数后，原本漂亮的输出可能不再漂亮。另外，正如你已看到的，字符串和数
# 的默认对齐方式不同。在一栏中同时包含字符串和数时，你可能想修改默认对齐方式。在指定宽
# 度和精度的数前面，可添加一个标志。这个标志可以是零、加号、减号或空格，其中零表示使用
# 0来填充数字。
length=50
print('❤'*length)
string="❤"*5
string+=' '*(length+25)
string+="❤"*5
print(string)
str='I love Fengyunxia'
strings="❤"*5+' '*ceil((length+25-len(str))/2)\
        +str+' '*ceil((length+25-len(str))/2)+"❤"*5
print(strings)
print(string)
print('❤'*length)

# 要指定左对齐、右对齐和居中，可分别使用<、>和^
# 。
print()
print('❤'*length)
print("{:<}".format('❤'*5)+"{:>80}".format('❤'*5))
# leng=ceil((len(str))/2+5)
# print(leng)
print("{:<}".format('❤'*5)+'{:^75}'.format('I love Fengyunxia')
      +"{:>5}".format('❤'*5))
print("{:<}".format('❤'*5)+"{:>80}".format('❤'*5))
print('❤'*length)
# print()



