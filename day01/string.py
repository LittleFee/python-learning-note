message="i love you fenGyunxia 哈哈"
print(message.title())#.title() 把字符串中每个单词的首字母大写，并且单词里的大写字母会被变成小写
print(message.upper())#.upper()把字符串中每个字母都大写
print(message.lower())#.lower()把字符串中每个字母都小写
uper_message=message.upper()
#存储数据时，方法lower() 很有用。很多时候，你无法依靠用户来提供正确的大小写，
#因此需要将字符串先转换为小写，再存储它们。以后需要显示这些信息时，再将其转换为最合适的大小写方式。
print(uper_message)

#字符串的拼接
first_name="kiwi"
last_name="qing"
full_name=first_name.title()+" "+last_name.title()
print(full_name)
print("Dear "+full_name+" It's time to go to bed")
