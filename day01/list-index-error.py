# 刚开始使用列表时，经常会遇到一种错误。假设你有一个包含三个元素的列表，却要求获取第四个元素
cars=['toyota','honda','audi']
# print(cars[3])  IndexError: list index out of range

# 如果需要访问最后一个的话，索引写-1就好
print(cars[-1].title())

# 仅当列表为空时，这种访问最后一个元素的方式才会导致错误
# test=[]
# print(test[-1])

# 发生索引错误却找不到解决办法时，请尝试将列表或其长度打印出来。列表可能与你以为的截然不同，在程序对其进行了动态处理时尤其如此。
# 通过查看列表或其包含的元素数，可帮助你找出这种逻辑错误。


