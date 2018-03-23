from module_sample import make_car as mc
car=mc('honda','gtr',speed=1000,pailiang='12L')
print(car)
# car2=make_car('sb','sc',dd=123)
# print(car2)

# 上面的import语句将函数make_car()重命名为mc()；在这个程序中，每当需要调用
# make_car()时，都可简写成mp()，而Python将运行make_car()中的代码，这可避免与这个程序
# 可能包含的函数make_car()混淆。