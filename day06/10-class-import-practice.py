# 9-10 导入Restaurant 类：将最新的Restaurant 类存储在一个模块中。在另一个文
# 件中，导入Restaurant 类，创建一个Restaurant 实例，并调用Restaurant 的一个方法，
# 以确认import 语句正确无误。

# 9-11 导入Admin 类：以为完成练习9-8 而做的工作为基础，将User、Privileges 和
# Admin 类存储在一个模块中，再创建一个文件，在其中创建一个Admin 实例并对其调用
# 方法show_privileges()，以确认一切都能正确地运行。



from restaurant import Restaurant
from admin import Admin

my_restaurant=Restaurant('kfc','food')
my_restaurant.describe_restaurant()

admin=Admin('Kiwi','qing','none')
admin.show.show_privileges()
