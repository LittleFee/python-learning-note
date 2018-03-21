message="test\n\ttable\n\t\tjim"
print(message)
# \n 换行  \t 制表符

message="  Ilobe "
end="end"
print(end+message+end)
print(end+message.lstrip()+end)#.lstrip()清除字符串左边的空格
print(end+message.rstrip()+end)#.rstrip()清除字符串右边的空格
print(end+message.strip()+end)#.strip()清楚字符串两边的空格
#演示清除字符串两边的空格 分别用到的方法：.lstrip()、.rstrip()、.strip()

