# 一个类继承(inherit)另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，
# 而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法
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

class E_car(Car):
    """电动车"""
    def __init__(self,maker,model,year,size):
        """初始化"""
        super().__init__(maker,model,year)
        # 父类也称为超类（superclass），名称super因此而得名。
        self.battery_size=size

    def show_battery_size(self):
        """显示电动车的电池容量"""
        print('It\'s has '+str(self.battery_size)+' kwh battery.')

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
        # 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子
        # 类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方
        # 法，而只关注你在子类中定义的相应方法。

e_car=E_car('Tesla','modelX',2017,80)
print(e_car.get_name_des())
e_car.show_battery_size()
e_car.fill_gas_tank()


# 将实例用作属性
# 使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文
# 件都越来越长。在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。你可以将大
# 型类拆分成多个协同工作的小类。
class Battery():
    """把电池提取出来成为一个小类"""
    def __init__(self):
        self.battery_size=70
        self.battery_life=100

    def show_battery_size(self):
        print('Size of battery is '+str(self.battery_size)+' kwh')

    def show_battery_life(self):
        print('Life of battery is '+str(self.battery_life)+' hours')

class E_car_2(Car):
    """实例作为属性演示"""
    def __init__(self,maker,model,year,size):
        """初始化"""
        super().__init__(maker,model,year)
        # 父类也称为超类（superclass），名称super因此而得名。
        self.batterry=Battery()

ecar=E_car_2('tesla','modelx',2017,80)
ecar.batterry.show_battery_size()