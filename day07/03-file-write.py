# 写入文件
file_name='file_write_w.txt'
with open(file_name,'w') as file_object:
    file_object.write('wwwwww')
# file_name='file_write_w.txt'
with open(file_name,'w+') as file_object:
    file_object.write('w+w+w+')
with open(file_name,'a') as file_object:
    file_object.write('aaaaaa')


# 注意 Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数
# str()将其转换为字符串格式。


# r只读，r+读写，不创建
#
# w新建只写，w+新建读写，二者都会将文件内容清零（以w方式打开，不能读出。w+可读写）
#
# r+：可读可写，若文件不存在，报错；w+: 可读可写，若文件不存在，创建
#
# r+进行覆盖写，a+追加写
#
# a：附加写方式打开，不可读；a+: 附加读写方式打开
#
# 若不存在会创建新文件的打开方式：a，a+，w，w+

with open(file_name,'w') as file_object:
    file_object.write('I love fyx\n')
    file_object.write('i love python')
    file_object.write('i love php')
    # file=file_object.read()
