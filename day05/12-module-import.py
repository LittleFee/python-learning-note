# 文件夹里有一个make_car.py的文件，里面只包含了自定义的make_car的函数
# 把文件名作为module名，在文件开头用 import make_car 引入
# 下面要使用到module的时候就用如下方式使用
# module_name.function_name()

import module_sample

car_info=module_sample.make_car('Benz','CL-200',Color='blue',Speed=150,length=5)
print(car_info)