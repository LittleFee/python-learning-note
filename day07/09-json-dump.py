# 存储数据
# json.dump()
import json

numbers=[2,4,5,6,8,9,0]
file_name='numbers.json'
with open(file_name,'w') as file_object:
    json.dump(numbers,file_object)