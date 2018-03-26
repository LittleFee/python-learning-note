class Restaurant():
    """餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        """类的初始化"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        """描述餐馆"""
        print('Our name is '+self.restaurant_name)
        print('We offer you '+self.cuisine_type)

    def open_restaurant(self):
        """餐馆开业通知"""
        print('Now we are opening')