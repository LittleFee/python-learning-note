# 字符串方法

# center
# 方法center通过在两边添加填充字符（默认为空格）让字符串居中。
print('*'*39)
print('*'*39)
print('I love fengyunxia'.center(39))
print('I love fengyunxia'.center(39,'*'))
print('*'*39)
print('*'*39)

# find
# 方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。
str='I love fengyunxia very very much'
print(str.find('v'))
print(str.find('a'))

# join
# join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素。
lists=['1','2','3','4']
str=''
print(str.join(lists))# 1234
str='-'
print(str.join(lists))# 1-2-3-4

dirs = ['', 'usr', 'bin', 'env']
print('C:'+"\\".join(dirs))

# replace
# 方法replace将指定子串都替换为另一个字符串，并返回替换后的结果。
# 区分大小写，且全部替换
str='ThIs is a good story and she is a good girl'
print(str.replace('is','was'))

# split
# split是一个非常重要的字符串方法，其作用与join相反，用于将字符串拆分为序列。
string='thisisastring'
print(string.split()) # ['thisisastring']
string='this a string'
print(string.split()) # ['this', 'a', 'string']


# translate
# 方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。
# 这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
# 然而，使用translate前必须创建一个转换表。这个转换表指出了不同Unicode码点之间的转
# 换关系。要创建转换表，可对字符串类型str调用方法maketrans，这个方法接受两个参数：两个
# 长度相同的字符串，它们指定要将第一个字符串中的每个字符都替换为第二个字符串中的相应字
# 符①。就这个简单的示例而言，代码类似于下面这样：
# >>> table = str.maketrans('cs', 'kz')
# 如果愿意，可查看转换表的内容，但你看到的只是Unicode码点之间的映射。
# >>> table
# {115: 122, 99: 107}
# 创建转换表后，就可将其用作方法translate的参数。
# >>> 'this is an incredible test'.translate(table)
# 'thiz iz an inkredible tezt'
# 调用方法maketrans时，还可提供可选的第三个参数，指定要将哪些字母删除。例如，要模
# 仿语速极快的德国口音，可将所有的空格都删除。
# >>> table = str.maketrans('cs', 'kz', ' ')
# >>> 'this is an incredible test'.translate(table)
# 'thizizaninkredibletezt'

table = str.maketrans('csi', 'kza')
print(table)
print('this is an incredible test'.translate(table))

# 判断字符串是否满足特定的条件
# 很多字符串方法都以is打头，如isspace、isdigit和isupper，它们判断字符串是否具有特定
# 的性质（如包含的字符全为空白、数字或大写）。如果字符串具备特定的性质，这些方法就返回
# True，否则返回False。
# 附录B：isalnum、isalpha、isdecimal、isdigit、isidentifier、islower、isnumeric、
# isprintable、isspace、istitle、isupper。
x='12'
print(x.isalnum())


