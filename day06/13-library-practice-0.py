# 9-13 使用OrderedDict：在练习6-4 中，你使用了一个标准字典来表示词汇表。请
# 使用OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加键—值对的
# 顺序一致。
from collections import OrderedDict

dict=OrderedDict()

dict['PHP']='超文本预处理器'
dict['range']='用于生成指定范围内的数字的函数'
dict['if']='条件判断语句'
dict['元组']='不可变的列表'
dict['字典']='类似php里的数组'
dict['迭代']='遍历'

for k,v in dict.items():
    print(k+':'+v)