# 10-11 喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用
# json.dump()将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打
# 印消息“I know your favorite number! It’s _____.”。
import json

num=input('你喜欢那个数字： ')
fname='num.json'
with open(fname,'w') as f_obj:
    json.dump(num,f_obj)