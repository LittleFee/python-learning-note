# print可以打印多个参数
fname = 'Kiwi'
lname = 'qing'
print(fname,lname)
# Kiwi qing
# 这样会在二者之间插入一个空格

print(fname,',',lname)
# Kiwi , qing
# 为了不有那么多的空格，你可以这样做：
print(fname+',',lname)

# 还可自定义分隔符
print(fname,lname,fname,sep='❤')
#Kiwi❤qing❤Kiwi

# 你还可自定义结束字符串，以替换默认的换行符。例如，如果将结束字符串指定为空字符串，
# 以后就可继续打印到当前行。
print('I love ',end='')
print('fengyunxia')
# I love fengyunxia


