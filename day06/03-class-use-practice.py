# 9-4 就餐人数：在为完成练习9-1 而编写的程序中，添加一个名为number_served
# 的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实例；打印有
# 多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个
# 方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
class Restaurant():
    """餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        """类的初始化"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        """描述餐馆"""
        print('Our name is '+self.restaurant_name)
        print('We offer you '+self.cuisine_type)

    def open_restaurant(self):
        """说明餐馆开张了"""
        print('Now we are opening')

    def set_number_served(self,number):
        """设置餐馆就餐人数"""
        if number > 0:
            self.number_served=number
        else:
            self.number_served = 0

    def increment_number_served(self,inc):
        """让餐馆人数递增"""
        if inc > 0:
            self.number_served+=inc
        else:
            self.number_served+=0

# 实例化这个类
my_restaurant=Restaurant('KFC','food')
# 打印就餐人数
print('There is '+str(my_restaurant.number_served)+' people eaten here.')
# 设置就餐人数并且打印
my_restaurant.set_number_served(23)
print('There is '+str(my_restaurant.number_served)+' people eaten here.')
# 增加就餐人数并打印
my_restaurant.increment_number_served(23)
print('There is '+str(my_restaurant.number_served)+' people eaten here.')



# 9-5 尝试登录次数：在为完成练习9-3 而编写的User 类中，添加一个名为
# login_attempts 的属性。编写一个名为increment_login_attempts()的方法，它将属性
# login_attempts 的值加1。再编写一个名为reset_login_attempts()的方法，它将属性
# login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts()多次。打印属
# 性login_attempts 的值，确认它被正确地递增；然后，调用方法reset_login_attempts()，
# 并再次打印属性login_attempts 的值，确认它被重置为0。
class User():
    """用户类"""
    def __init__(self, fname, lname, des):
        """初始化用户类"""
        self.fname=fname
        self.lname=lname
        self.des=des
        self.login_attempts=0

    def describe_user(self):
        """描述用户"""
        print('Name:'+self.fname.title()+' '+self.lname.title())
        print('Other information:\n'+self.des)

    def greet_user(self):
        """给用户打招呼"""
        print('Hola '+self.fname.title()+' '+self.lname.title()+'!')

    def increment_login_attempts(self):
        """将尝试登录次数+1"""
        self.login_attempts+=1

    def reset_login_attempts(self):
        """重置尝试登录次数"""
        status=input('Rest?(yes for continue) ')
        if status=='yes':
            self.login_attempts=0

user=User('KIWI','QING','sex=male')
user.increment_login_attempts()
print(user.fname.title()+' attempt login '+str(user.login_attempts)+' times')
user.increment_login_attempts()
print(user.fname.title()+' attempt login '+str(user.login_attempts)+' times')
user.increment_login_attempts()
print(user.fname.title()+' attempt login '+str(user.login_attempts)+' times')
user.reset_login_attempts()
print(user.fname.title()+' attempt login '+str(user.login_attempts)+' times')


