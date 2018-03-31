# pop
# 方法pop可用于获取与指定键相关联的值，并将该键-值对从字典中删除。
d={'x':2,'y':1}
print(d.pop('x'))
print(d)

# popitem
# 方法popitem类似于list.pop，但list.pop弹出列表中的最后一个元素，而popitem随机地弹
# 出一个字典项，因为字典项的顺序是不确定的，没有“最后一个元素”的概念。如果你要以高效
# 地方式逐个删除并处理所有字典项，这可能很有用，因为这样无需先获取键列表。
c={'x':2,'y':1,'z':34,'f':2,'j':1,'a':34}
print(c.popitem())
print(c)
d = {}
v=d.setdefault('name', 'N/A')
print(v)
print(d)


d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}
x = {'title': 'qingwei.tech'}
y = {'url': 'https://www.qingwei.tech'}

d.update(x)
d.update(y)
print(d)
# {'title': 'qingwei.tech', 'url': 'https://www.qingwei.tech',
# 'changed': 'Mar 14 22:09:15 MET 2016'}
z={'hehe':'eeee'}
d.update(z)
print(d)
# {'title': 'qingwei.tech', 'url': 'https://www.qingwei.tech',
# 'changed': 'Mar 14 22:09:15 MET 2016', 'hehe': 'eeee'}

