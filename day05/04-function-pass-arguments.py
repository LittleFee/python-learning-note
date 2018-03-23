# 位置实参
# 你调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，
# 最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hashiqi','Erha')
# 这个函数的定义表明，它需要一种动物类型和一个名字。调用describe_pet()时，需
# 要按顺序提供一种动物类型和一个名字。例如，在前面的函数调用中，实参'hashiqi'存储在形
# 参animal_type中，而实参'Erha'存储在形参pet_name中。在函数体内，使用了这两个形
# 参来显示宠物的信息。


# 关键字实参:关键字实参是传递给函数的名称—值对 看栗子
# 还是上面的函数
describe_pet(animal_type='cat',pet_name='Miaomi')
describe_pet(pet_name='Miaomiao',animal_type='cat')
# 也就是使用了关键字实参就不用在意参数的位置关系

# But 如果关键字实参以以下方式就不行，因为这样操作实际还是位置实参，
# 只不过以变量的形式给了一个实参罢了
pet_name='Miaomiaomi'
animal_type='cat'
describe_pet(pet_name,animal_type)


# 默认值,
# def describe_pet_2(animal_type='dog',pet_name):
# 有默认值的参数不能放在没有默认值的前面，上面的代码会报错

def describe_pet_2(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet_2('Erha')

# 以上调用方式都是对的，按自己需求正确使用就OK
# 位置实参 关键字实参 默认值

