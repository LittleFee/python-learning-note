# 返回值
# 返回一个整洁的姓名
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+' '+last_name
    return full_name.title()

full_name=get_formatted_name('kiwi','qing')
print(full_name)


# 让实参变成可选的
# 譬如 中间名 这个是一个可选项

def get_formatted_name_middle(first_name,last_name,middle_name=''):
    """返回可以输入中间名的整洁姓名"""
    if middle_name:
        full_name = first_name +' '+middle_name+' ' + last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()

full_name=get_formatted_name_middle('wei','qing')
print(full_name)
full_name=get_formatted_name_middle('wei','qing','feng')
print(full_name)

# 返回字典
def build_person(fistname,lastname):
    """返回一个人的姓名的字典"""
    dict={'First':fistname.title(),'last':lastname.title()}
    return dict
dict=build_person('kiwi','qing')
print(dict)

def end():
    """结束前打印语句"""
    print('Opps...Byebye')


while True:
    print('Tell me your name (enter q to quit)')
    fname=input('OK tell me your first name')
    if fname.lower()=='q':
        end()
        break
    lname=input("OK now tell me the last name")
    if lname=='q':
        end()
        break
    print('Your full name is '+get_formatted_name(fname,lname))