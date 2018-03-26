"""一个可用于表示汽车的类"""

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