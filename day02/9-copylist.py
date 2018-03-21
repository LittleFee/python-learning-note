fr_foods=['noodles','rice','bread','bannaner']
my_foods=fr_foods[:]
print('my food :')
print(my_foods)
print('my friend food :')
print(fr_foods)
my_foods.append('mango')
fr_foods.append('milk')
print('my food :')
print(my_foods)
print('my friend food :')
print(fr_foods)
his_food=my_foods
print('his')
print(his_food)
my_foods.append('watermelon')
print(his_food)#['noodles', 'rice', 'bread', 'bannaner', 'mango', 'watermelon'] 这就是没有使用切片的情况