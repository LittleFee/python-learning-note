# 传递任意数量的实参，实际传递的是一个元组
# 例如不知道要多少配料，这里要求循环打印出用户提供的配料
def print_peiliao(*peiliao):
    """打印配料（元组）"""
    print(peiliao)
print_peiliao('辣椒','面粉','鸡蛋','芝麻')

def print_peiliao(*peiliao):
    """分别打印配料"""
    for peil in peiliao:
        print(peil)
print_peiliao('辣椒','面粉','鸡蛋','芝麻')

# 结合使用位置实参和任意数量实参
def make_pizza(size,*peiliaos):
    """任意数量的实参"""
    print('Someone ordered a '+str(size)+' pizza and need these peiliao:')
    for peiliao in peiliaos:
        print('-'+peiliao)

make_pizza(23,'辣椒面','胡萝卜','榴莲','芥末')


# 使用任意数量的关键字实参
# 创建一个字典，其中包含我们知道的有关用户的一切
def user_profile(fname,lname,**canshu):
    """收集用户所有信息"""
    profile={}
    profile['Firstname']=fname
    profile['Lastname']=lname
    for k,v in canshu.items():
        profile[k]=v
    return profile

profile=user_profile('Wei','qing',localtion='chengdu',sex='male',age=25)
print(profile)