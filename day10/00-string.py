from math import pi

strings='{} love {} fyx'
print(strings.format('I','you'))
# 字符串格式设置，按顺序


string="{0} {1} {2} {3} {0} {1}"
print(string.format('to','be','or','not'))
# 字符串格式设置，按索引


str="{name} is approximately {value:.2f}."
print(str.format(value=pi, name="π") )
# π is approximately 3.14.
# 用名称来格式化，用冒号:把名称和格式说明符.2f 分开 表示保留两位小数

str="{name} is approximately {value}."
print(str.format(value=pi, name="π") )
# π is approximately 3.141592653589793.

