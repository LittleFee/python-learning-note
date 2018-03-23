# 你还可以导入模块中的特定函数
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import function_0, function_1, function_2
# 若使用这种语法，调用函数时就无需使用句点。由于我们在import语句中显式地导入了函数
# make_car()，因此调用它时只需指定其名称。
from module_sample import make_car
car=make_car('volvo','s40',speed=1000)
print(car)