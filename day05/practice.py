def user_profile(fname,lname,**canshu):
    """收集用户所有信息"""
    profile={}
    profile['Firstname']=fname
    profile['Lastname']=lname
    for k,v in canshu.items():
        profile[k]=v
    return profile