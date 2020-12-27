#工厂设计模式 ------>用户需要一个新的类型时，直接添加一个类，就可以而不用去修改已知的类
#设计步骤 -   1,商场调用工厂对象为属性 2，工厂按名称返回一个类
#实质：通过类与类循环调用另，将指向特定的类的路径最简化


#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
#设置一个模板类
class Car(object):
    @staticmethod
    def run():
        print("快快地跑")
    @staticmethod
    def stop():
        print("慢慢地停")

class Benz(Car):
    pass

class Baoma(Car):
    pass
#-------------------------------------------------------------------------------------------------------------------
#设置一个工厂类
class Carfortory(object):
    def new_car(self, name):
        #工厂生产，如果调用new car方法，调用一次类
        if name == "Benz":
            return Benz()
        if name == "Baoma":
            return Baoma()

#-------------------------------------------------------------------------------------------------------------------
#设置一个销售类
class CarStore(object):
    def __init__(self, fortory):
        self.fortory = fortory
    def order(self, name):
        return self.fortory.new_car(name)

fortory1 = Carfortory()
store1 = CarStore(fortory1)
car_01 = store1.order("Benz") #本质上返回的是一个特定的类
car_01.run()
car_01.stop()


