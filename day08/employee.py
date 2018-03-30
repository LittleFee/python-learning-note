# 11-3 雇员：编写一个名为 Employee 的类，其方法__init__()接受名、姓和年薪，并
# 将它们都存储在属性中。编写一个名为 give_raise()的方法，它默认将年薪增加 5000
# 美元，但也能够接受其他的年薪增加量。
# 为 Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_
# raise()和 test_give_custom_raise()。使用方法 setUp()，以免在每个测试方法中都创
# 建新的雇员实例。运行这个测试用例，确认两个测试都通过了。

class Employee():
    """雇员类"""
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def give_rise(self,add_salary=5000):
        """给雇员加年薪，默认5000"""
        self.salary+=add_salary