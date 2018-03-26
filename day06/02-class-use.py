# 使用类和实例
class Car():
    """描述小汽车，包括年份、制造商和型号"""
    def __init__(self,year,maker,model):
        """初始化汽车属性"""
        self.year=year
        self.maker=maker
        self.model=model
        self.odometer_reading=0
        # 给一个路码表初始读数0
    def get_name_des(self):
        """描述汽车"""
        long_name=str(self.year)+' '+self.maker+' '+self.model
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

# 初始化一辆2018年的BMW i3
new_car=Car(2018,'BMW','i3')
print(new_car.get_name_des())
new_car.get_odometer_reading()

# 直接修改路码表的读数（属性）为234，并且打印
new_car.odometer_reading=234
new_car.get_odometer_reading()

# 使用类内部的方法修改路码表的读数（属性）为438
new_car.update_odometer(438)
new_car.get_odometer_reading()

new_car.update_odometer(146)
new_car.get_odometer_reading()

new_car.add_odometer(146)
new_car.get_odometer_reading()

new_car.add_odometer(-234)
new_car.get_odometer_reading()
