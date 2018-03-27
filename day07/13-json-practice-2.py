# 10-12 记住喜欢的数字：将练习10-11 中的两个程序合而为一。如果存储了用户喜
# 欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运
# 行这个程序两次，看看它是否像预期的那样工作。
import json

fname = 'num.json'
try:
    with open(fname) as f_obj:
        num = json.load(f_obj)
except FileNotFoundError:
    num = input('你喜欢那个数字： ')
    with open(fname, 'w') as f_obj:
        json.dump(num, f_obj)
else:
    print('I know your favorite number! It\'s ' + num)