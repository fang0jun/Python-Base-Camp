class Cat():
    def __init__(self,cat_name,cat_color):
        self.name = cat_name
        self.color = cat_color
        print("我是%s，我是一只猫"% self.name)
    def eat(self):
        print("我要鱼喵")
    def __del__(self):
        print("我走了喵%s"%self.name)

#自动执行初始化
cat = Cat("MIAO","red")
print(cat.name)

#del可以删除一个对象
#del cat
# #自动执行销毁后语句
# cat.kill()

print("-" * 50)