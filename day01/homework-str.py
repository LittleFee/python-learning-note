#个性化消息： 将用户的姓名存到一个变量中，并向该用户显示一条消息
# name_1=input("Input your name please \n")
name_1="kiwi"
print("Hello "+name_1.title()+",How's your day")

#调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
# name_2=input("Input your name please \n")
name_2="feng Yun xiA"
print(name_2.lower())
print(name_2.upper())
print(name_2.title())

#名言： 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应包括引号
words_1="宝宝说'I love you baby'"
words_2='宝宝说"I love you baby"'
print(words_1)
print(words_1.title())
print(words_2)
print(words_2.title())

#名言2： 重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建要显示的消息，并将其存储在变量message 中，然后打印这条消息。
famous_person="宝宝"
message1="'I love You'"
message2='"I Love you"'
print(famous_person+"说:"+message1)
print(famous_person+"说:"+message1.title())
print(famous_person+'say:'+message2)
print(famous_person+'say:'+message2.title())

#剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
#打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。
namestrip="   Feng\nyun\txia   "
print(namestrip)
print(namestrip.lstrip())
print("..........")
print(namestrip.rstrip())
print("..........")
print(namestrip.strip())


