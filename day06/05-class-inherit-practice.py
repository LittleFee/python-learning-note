# 9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的
# 类，让它继承你为完成练习9-1 或练习9-4 而编写的Restaurant 类。这两个版本的
# Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于
# 存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个
# IceCreamStand 实例，并调用这个方法。

class Restaurant():
    """餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        """类的初始化"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        """描述餐馆"""
        print('Our name is '+self.restaurant_name)
        print('We offer you '+self.cuisine_type)

    def open_restaurant(self):
        """餐馆开业通知"""
        print('Now we are opening')

class IceCreamStand(Restaurant):
    """冰淇淋小店"""
    def __init__(self,restaurant_name,cuisine_type,flavors):
        """初始化"""
        super().__init__(restaurant_name,cuisine_type)# 将子类与父类连接
        self.flavors=flavors

    def print_icecream(self):
        """打印所有的冰淇淋"""
        print('we offer :')
        for item in self.flavors:
            print('-'+item)


icecreams=[]# 冰淇淋列表，由用户输入
while True:
    icecream=input('say some icecream (no for break):')
    if icecream=='no':
        break
    else:
        icecreams.append(icecream)

iceCreamStand=IceCreamStand('kiwi','icecream',icecreams)
iceCreamStand.open_restaurant()
iceCreamStand.print_icecream()


# 9-7 管理员：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为
# 完成练习9-3 或练习9-5 而编写的User 类。添加一个名为privileges 的属性，用于存
# 储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的
# 列表。编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin
# 实例，并调用这个方法。
class User():
    """用户类"""
    def __init__(self, fname, lname, des):
        """初始化"""
        self.fname=fname
        self.lname=lname
        self.des=des

    def describe_user(self):
        """描述用户信息"""
        print('Name:'+self.fname.title()+' '+self.lname.title())
        print('Other information:\n'+self.des)

    def greet_user(self):
        """给用户个性化的问候"""
        print('Hola '+self.fname.title()+' '+self.lname.title()+'!')

class Admin(User):
    """Admin权限类"""
    def __init__(self,fname,lname,des):
        super().__init__(fname,lname,des)
        self.privileges=['can add post','can delete post','can ban user']
        # self.show=Privileges()
    def show_privileges(self):
        """显示管理员权限"""
        self.greet_user()
        print('Your privileges are: ')
        for item in self.privileges:
            print('\t'+item.title())

admin=Admin('Kiwi','qing','sex:male')
admin.show_privileges()

# 9-8 权限：编写一个名为Privileges 的类，它只有一个属性——privileges，其中
# 存储了练习9-7 所说的字符串列表。将方法show_privileges()移到这个类中。在Admin
# 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法
# show_privileges()来显示其权限。
class Admins(User):
    """Admin权限类"""
    def __init__(self,fname,lname,des):
        super().__init__(fname,lname,des)
        self.show=Privileges()

class Privileges():
    """权限列表类"""
    def __init__(self):
        self.privileges = ['can add posts', 'can delete posts', 'can ban user']

    def show_privileges(self):
        """显示管理员权限"""
        # self.greet_user()
        print('Your privileges are: ')
        for item in self.privileges:
            print('\t'+item.title())



admin2=Admins('tina','wang','sex:female')
admin2.show.show_privileges()



# 9-9 电瓶升级：在本节最后一个electric_car.py 版本中，给Battery 类添加一个名为
# upgrade_battery()的方法。这个方法检查电瓶容量，如果它不是85，就将它设置为85。
# 创建一辆电瓶容量为默认值的电动汽车，调用方法upgrade_battery()，然后对电瓶进行升级，
# 并再次调用get_range()。你会看到这辆汽车的续航里程增加了。

class Car():
    """描述小汽车，包括年份、制造商和型号"""
    def __init__(self,maker,model,year):
        """初始化汽车属性"""
        self.maker=maker
        self.model=model
        self.year = year
        self.odometer_reading=0
        # 给一个路码表初始读数0
    def get_name_des(self):
        """描述汽车"""
        long_name=self.maker+' '+self.model+' '+str(self.year)
        return long_name

    def get_odometer_reading(self):
        """打印路码表读数"""
        print('The odometer reading is '+str(self.odometer_reading)+' now')

    def update_odometer(self,mile):
        """修改路码表读数+防止往回调路码表"""
        # self.odometer_reading=mile
        if mile >= self.odometer_reading:
            self.odometer_reading=mile
        else:
            print("You can't roll back an odometer!")

    def add_odometer(self,mile):
        """将里程表读数增加指定的量"""
        if mile >= 0:
            self.odometer_reading+=mile
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        """为演示重写父类方法而添加"""
        print("OK Now!")

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 2700
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size=85

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

car=ElectricCar('Tesla','modleX',2016)
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()