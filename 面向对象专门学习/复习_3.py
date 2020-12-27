# 内置函数dir() 的使用，查看对象可以调用的方法  对象-函数数据变量都是一个对象
# 下滑线内置方法和属性  __new__ __init__ __del__ __str


#     类的创建和其属性的设置
# 所有类创造的一步  -- 需求分析（造句，提词） - 名词-类 形容词（固定/随机）-属性  动词-方法
# 面对对象编程的特点---封装 （主程序中只让对象去工作，而不关心具体细节）
# 给类添加方法 1，对于不同的对象，代码是相似还是一致 2,方法所用到的参数是否是本类封装的属性
# 给类增加属性 1，对于不同对象，属性的调用是固定还是随机
#   ---创建对象会自动调用两个内置方法  ---分配空间方法new  ---初始化方法init(为属性设置初始值)
#   ---在init中用self.xxx = xxx ，获得(固定)属性
#   ---若你的属性是不固定的（由你而定）的，则self.xxx = 形参

"""

两个初始化方法
del 销毁之前自动最后一次调用（程序完整运行一次后也会进行一次销毁）
str 给对象的打印内容化妆（此方法必须要返回一个字符串）

"""

class Cat(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s爱吃鱼"%self.name)

    def drink(self):
        print("%s要喝水" % self.name)

    def __str__(self):
        return "我是小猫[%s]"%self.name

tom = Cat("Tom")
lazy_cat = Cat("LAZY_CAT")

lazy_cat.eat()
tom.drink()
print(tom)