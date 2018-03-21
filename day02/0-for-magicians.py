# 利用for循环打印列表里的内容
magicians=['tom','larry','jim','timor']
print('The name list of magicians:')
for magician in magicians:
    print('\t'+magician.title()+',we are looking forward your next show')
    print('\tGreat!')

print('=====End=====')

# 命名规则：
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:
# 使用单数和复数式名称，可帮助你判断代码段处理的是单个列表元素还是整个列表。