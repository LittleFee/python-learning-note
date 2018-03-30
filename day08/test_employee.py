import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """测试employee.py(Employee)"""
    def setUp(self):
        self.fname='Kiwi'
        self.lname='Qing'
        self.salary=5000
        self.employeeObj=Employee(self.fname,self.lname,self.salary)

    def test_give_default_raise(self):
        """测试是否是默认加薪后的年薪"""
        self.employeeObj.give_rise()
        raised_salary=self.employeeObj.salary
        hope_salary=self.salary+5000
        self.assertEqual(hope_salary,raised_salary)

    def test_give_custom_raise(self):
        """测试是否是自定义加薪后的年薪"""
        self.employeeObj.give_rise(1000)
        raised_salary = self.employeeObj.salary
        hope_salary=self.salary+1000
        self.assertEqual(hope_salary,raised_salary)
unittest.main()