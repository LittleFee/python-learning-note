from car import ElectricCar

my_e_car=ElectricCar('Tesla','p100',2017)
print(my_e_car.get_name_des())
my_e_car.battery.get_range()
my_e_car.battery.battery_size=85
my_e_car.battery.get_range()