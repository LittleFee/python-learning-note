#3-1 姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
names=['Tina','Emily','Liam','Stanley']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

#3-2 问候语： 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
words="Good Morning "
print(words+names[-4])
print(words+names[1])
print(words+names[2])
print(words+names[3])

# 3-3 自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。
# 根据该列表打印一系列有关这些通勤方式的宣言，如“I wouldlike to own a Honda motorcycle”。
way=['bike','train','car']
handle=["drive ",'take ','ride ']
print("I wold like to "+handle[-1]+'a '+way[0])
print("I would like to "+handle[1]+'a '+way[1])
print("I would like to "+handle[0]+'a '+way[-1])