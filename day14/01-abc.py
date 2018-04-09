# 抽象基类
# 抽象类是不能（至少是不应该）实例化的类，其职责是定义子类应实
# 现的一组抽象方法。
from abc import ABC, abstractmethod
class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

# talk=Talker()
# 抽象类（即包含抽象方法的类）最重要的特征是不能实例化。


class ITalk(Talker):
    # pass # 由于没有重写方法talk，因此这个类也是抽象的，不能实例化。
    def talk(self):
        print('Hi it\'s me')



italk=ITalk()
italk.talk()

