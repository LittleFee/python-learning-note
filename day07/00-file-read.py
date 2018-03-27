# 使用关键字with时，open()返回的文件对象只在with代码块内可用。
with open('pi_digits.txt') as file_object:
    # print(file_object)
    content=file_object.read()
    print(content)
    # read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。要删
    # 除多出来的空行，可在print语句中使用rstrip()
    print(content.rstrip())

# 逐行读取
file_name='pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())
        # 由于
print('===========')
# 使用关键字with时，open()返回的文件对象只在with代码块内可用。
with open(file_name) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line)
print('===========')
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))
