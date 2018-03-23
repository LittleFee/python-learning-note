def make_car(maker,model,**canshu):
    """造车"""
    car_info={}
    car_info['Maker']=maker.title()
    car_info['model']=model.title()
    for k,v in canshu.items():
        car_info[k]=v
    return car_info

def user_profile(fname,lname,**canshu):
    """收集用户所有信息"""
    profile={}
    profile['Firstname']=fname
    profile['Lastname']=lname
    for k,v in canshu.items():
        profile[k]=v
    return profile