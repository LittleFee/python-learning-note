# 9-1 餐馆：创建一个名为Restaurant 的类，其方法__init__()设置两个属性：
# restaurant_name 和cuisine_type。创建一个名为describe_restaurant()的方法和一个
# 名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，
# 指出餐馆正在营业。
# 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述
# 两个方法。
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
        print('Now we are opening')

my_restaurant=Restaurant('Addlove','Cake')
print('Our name is '+my_restaurant.restaurant_name.title())
print('Our cuisine type is '+my_restaurant.cuisine_type.title())
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 9-2 三家餐馆：根据你为完成练习9-1 而编写的类创建三个实例，并对每个实例调
# 用方法describe_restaurant()。
your_restaurant=Restaurant('H&N','Noddle')
your_restaurant.describe_restaurant()
our_restaurant=Restaurant('KFC','Chicken')
our_restaurant.describe_restaurant()
restaurant=Restaurant('McDownload','Coder food')
restaurant.describe_restaurant()


# 9-3 用户：创建一个名为User 的类，其中包含属性first_name 和last_name，还有
# 用户简介通常会存储的其他几个属性。在类User 中定义一个名为describe_user()的方
# 法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化
# 的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。

class User():
    """用户类"""
    # def __init__(self,fname,lname,**des):
    def __init__(self, fname, lname, des):
        self.fname=fname
        self.lname=lname
        self.des=des
        # for k,v in des.items():
        #     self.dess[k]=v

    def describe_user(self):
        print('Name:'+self.fname.title()+' '+self.lname.title())
        print('Other information:\n'+self.des)

        # for k,v in self.dess.items():
        #     print('\t'+k+':'+str(v))

    def greet_user(self):
        print('Hola '+self.fname.title()+' '+self.lname.title()+'!')

me=User('Kiwi','Qing','sex:male')
me.describe_user()
me.greet_user()

you=User('Shine','Feng','sex:female')
you.describe_user()
you.greet_user()

