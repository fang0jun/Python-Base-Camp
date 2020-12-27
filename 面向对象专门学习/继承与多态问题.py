#子类继承父类所有代码            ---类的继承
#super调用父类方法/形参调用对象方法 (这是多态)        --方法的继承
#改写父类方法 （重写与方拓展super()）
#方法---方法重写 super在子类中从父类里调用方法 形参直接在对象里调用方法

class Dog:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("使用父类Dog的eat方法eat")
    def drink(self):
        print("使用父类Dog的drink方法drink")



class XiaoTianDog(Dog):
    #在方法里面调用父类的方法
    def eat(self):
        print("使用神犬子类的eat方法eat")

    def new_drink(self,fudog):
        fudog.drink()

    #在方法里面调用一个对象的方法（要以对象为形参）



class person():
    def __init__(self, name):
        self.name = name
    def play_with_dog(self, with_who):
        with_who.eat()
        print("%s与%s一起玩"%(self.name,with_who.name))




xiaoming = person("xiaoming")
dog0 = Dog("正常狗")
dog = XiaoTianDog("神犬")
dog.drink()
dog.new_drink(dog0)

# xiaoming.play_with_dog(dog)
