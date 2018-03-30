# 11-1 城市和国家：编写一个函数，它接受两个形参：一个城市名和一个国家名。这
# 个函数返回一个格式为 City, Country 的字符串，如 Santiago, Chile。将这个函数存储
# 在一个名为 city _functions.py 的模块中。
# 创建一个名为 test_cities.py 的程序，对刚编写的函数进行测试（别忘了，你需要导
# 入模块 unittest 以及要测试的函数）。编写一个名为 test_city_country()的方法，核实
# 使用类似于'santiago'和'chile'这样的值来调用前述函数时，得到的字符串是正确的。
# 运行 test_cities.py，确认测试 test_city_country()通过了。

# 11-2 人口数量：修改前面的函数，使其包含第三个必不可少的形参 population，并
# 返回一个格式为 City, Country – population xxx 的字符串，如 Santiago, Chile –
# population 5000000。运行 test_cities.py，确认测试 test_city_country()未通过。
# 修改上述函数，将形参 population 设置为可选的。再次运行 test_cities.py，确认测
# 试 test_city_country()又通过了。
# 再编写一个名为 test_city_country_population()的测试，核实可以使用类似于
# 'santiago'、'chile'和'population=5000000'这样的值来调用这个函数。再次运行
# test_cities.py，确认测试 test_city_country_population()通过了。
import unittest
from city_country import city_country

class CityTestCase(unittest.TestCase):
    """测试city_country函数"""
    def test_city_country(self):
        back=city_country('santiago','chile')
        self.assertEqual(back,'Santiago, Chile')

    def test_city_country_population(self):
        back=city_country('santiago','chile',10000)
        self.assertEqual(back,'Santiago, Chile - population 10000')

unittest.main()