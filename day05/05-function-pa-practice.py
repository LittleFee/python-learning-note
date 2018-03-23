# 8-3 T 恤：编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T 恤上
# 的字样。这个函数应打印一个句子，概要地说明T 恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件T 恤；再使用关键字实参来调用这个函数。

def make_shirt(size,symbol):
    """打印T恤"""
    print('This is a: '+size+' T-shirt and print with: '+symbol)
make_shirt('XL','PHP is the best language(逃')

make_shirt(symbol='Life is too short, I code with Python',size='XXL')

# 8-4 大号T 恤：修改函数make_shirt()，使其在默认情况下制作一件印有字样“I love
# Python”的大号T 恤。调用这个函数来制作如下T 恤：一件印有默认字样的大号T 恤、
# 一件印有默认字样的中号T 恤和一件印有其他字样的T 恤（尺码无关紧要）。

def make_shirt_2(size='L',symbol='I love Python'):
    """有默认值的打印T恤"""
    print('This is a: '+size+' T-shirt and print with: '+symbol)

make_shirt_2()
make_shirt_2('M')
make_shirt_2(symbol='I love FYX')


# 8-5 城市：编写一个名为describe_city()的函数，它接受一座城市的名字以及该城
# 市所属的国家。这个函数应打印一个简单的句子，如Reykjavik is in Iceland。给用
# 于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城
# 市不属于默认国家。

def describe_city(city,country='china'):
    """打印国家城市名"""
    print(city.title()+' is in '+country.title())

describe_city('mianyang')
describe_city(country='japan',city='tokoyo')
describe_city('paris','france')