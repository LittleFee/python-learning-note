import json

fname='num.json'
with open(fname) as f_obj:
    num=json.load(f_obj)
print('I know your favorite number! It\'s '+num)