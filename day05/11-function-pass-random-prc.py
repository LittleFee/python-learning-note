# 8-12 三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个
# 函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点
# 的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
def order_san(*foods):
    """打印食材"""
    print('客户预定了如下食材：')
    for food in foods:
        print('-'+food)

order_san('红豆','蜂蜜','牛肉')
order_san('猪肉','大葱')
order_san('猪肉','大葱','蒜苗')


# 8-13 用户简介：复制前面的程序user_profile.py，在其中调用build_profile()来
# 创建有关你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键值对。
def user_profile(fname,lname,**canshu):
    """收集用户所有信息"""
    profile={}
    profile['Firstname']=fname
    profile['Lastname']=lname
    for k,v in canshu.items():
        profile[k]=v
    return profile

profile=user_profile('Wei','qing',localtion='chengdu',sex='male',age=25)
print(profile)


# 8-14 汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接
# 受制造商和型号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的
# 信息，以及两个名称—值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。

def make_car(maker,model,**canshu):
    """造车"""
    car_info={}
    car_info['Maker']=maker.title()
    car_info['model']=model.title()
    for k,v in canshu.items():
        car_info[k]=v
    return car_info
car_info=make_car('Benz','CL-200',Color='blue',Speed=150,length=5)
print(car_info)