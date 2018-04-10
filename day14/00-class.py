# 多个超类（父类）
class Caculater:
    def cacu(self,exp):
        self.value=eval(exp)

class Talker:
    def talk(self):
        print('Value is ' + str(self.value))
class Child(Caculater,Talker):
    pass

child=Child()
child.cacu('3+2-4')
child.talk()
# Value is 1