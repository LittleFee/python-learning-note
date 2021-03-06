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