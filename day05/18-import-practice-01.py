# 8-16 导入：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一
# 个文件中。在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# import practice
# profile=practice.user_profile('qing','wei',age=10,height=177)
# print(profile)

# from practice import user_profile
# pro=user_profile('qing','wei',sex='male')
# print(pro)

# from practice import user_profile as up
# pro=up('name','name',age=34)
# print(pro)

# import practice as pr
# pro=pr.user_profile('jjj','ccc',weight=89)
# print(pro)
from practice import *
pro=user_profile('gg','mm',city='chengdu')
print(pro)

