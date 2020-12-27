class Person:
    def __init__(self,p_name,p_weight):
        self.name = p_name
        self.weight = p_weight
    def run(self):
        print("running weight - 0.5！\n")
        self.weight -= 0.5
    def eat(self):
        print("running weight + 1！\n")
        self.weight +=  1
    def __str__(self):
        return "my name is %s,now_weight: %0.2f" %(self.name,self.weight)

xiaoming = Person("小明",120.0)
xiaomei = Person("小美",100.0)

xiaoming.eat()
xiaoming.eat()
xiaoming.eat()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaomei.run()
xiaomei.eat()
print(xiaoming)
print(xiaomei)
