from user import User

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