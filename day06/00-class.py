class Dog():
    """创建一个简单的小狗类"""
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def set(self):
        """描述小狗坐下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """描述小狗已经打滚了"""
        print(self.name.title()+' has rolled over')

my_dog=Dog('cK',12)
print('The name of my dog is '+my_dog.name.title())
print('My dog '+my_dog.name.title()+' is '+str(my_dog.age)+' now')
my_dog.set()
my_dog.roll_over()

you_dog=Dog('mq',38)
print(you_dog.name.title()+' is your dog')
print('It is a '+str(you_dog.age)+' years old now')