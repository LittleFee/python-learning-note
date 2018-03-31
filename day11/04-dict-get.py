# get
# 方法get为访问字典项提供了宽松的环境。通常，如果你试图访问字典中没有的项，将引发
# 错误。使用get来访问不存在的键时，没有引发异常，而是返回None。你可指定“默认”
# 值，这样将返回你指定的值而不是None。

d={'age':19,'addr':'chengdu'}
# print(d['name'])
print(d.get('name'))# None
print(d.get('sex','N/A'))# N/A
