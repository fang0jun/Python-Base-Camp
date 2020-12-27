import plane_sprite   #---调用时需要模块名
from plane_sprite import module_1
from plane_sprite impot *   #---调用时不需要模块名

"""

模块导入的导入顺序：先当前目录 / 后系统目录  （故不要重名）
if __name__ == "__main__"   只在本文件中进行测试

文件被当作模块导入时，所有没有缩进的代码都会被执行一遍 // 若要测试则使用 if __name__ == "__main__"
（使用__name__属性---保存一系列字符串，在当前执行文件中为__main__ 在被导入文件中为所在模块的模块名）

"""
========================================================
"""

多态的意义
一种方法有多种姿态（对于不同子类来说），但可以通过父类来自我调用
一法多态，以父调自我


实现方法：在外部调用了父类中的方法，并以该父类对象或子类对象为参数 //

解释：
当你需要很多子类调用一种方法时，直接调用父类的那种方法就好了
以此来让该父类对象或子类对象自动调用自己的方法（以一包多，多种姿态）

"""


class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):
    def run(self):
        print("Dog is running")

dog1 = Animal()
dog_real = Dog()


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog1)
run_twice(dog_real)




=================================================
"""

异常的传递

"""

def demo1():
    return int(input("请输入一个整数："))

def demo2():
    return demo1()
try:
    print(demo2())

except Exception as result:
    print("未知错误。。。%s" % result)
else:
    print("继续程序运行")
finally:
    print("-" * 20)
#真正的异常出现在第8行，但是把异常交给了13行（主程序中） 8 - 11 - 13
#利用异常的传递性，把异常传递到主程序，在主程序中捕获异常,以精简代码


=======================================================
"""

主动抛出异常   ---由需求所决定的异常
1，创建异常对象，2，抛出异常对象

需求：
用户输入用户名，用户名必须大于等于8位数否则 抛出异常

"""


def into():
    password = input("请输入密码：")
    if len(password) >= 8:
        return password
    error = Exception("密码长度不够")   # 接受一个元组，作为异常的名称
    raise error


try:
    print(into())

except Exception as result:
    print(result)


==================================================

"""

对于异常的处理 --- 让错误不影响代码的继续运行，而是先 抛出 异常  ---它将在程序中传递

结构 try --- except（except Exception as result） --- else --- finally
对于可能出错的地方 加入try获取错误
对于可能出现的错误类型 加入except收集不同类型的错误 + 再以except Exception as result囊括所有类型
                 else：针对无错运行时执行的代码块
"""

try:
    num = int(input("请输入一个整数"))
    number = 8 / num

    print(number)

except ValueError as e:
    print("请老老实实地输入一个整数,别再输入%s" % e)
except Exception as result:
    print("未知错误 %s" % result)

else:
    print("执行成功继续向下")
finally:
    print("无论如何我都在")


=============================================================
"""
面对对象高级编程

实例属性属于各个实例所有，互不干扰；
类属性属于类所有，所有实例共享一个属性；


使用@property进行属性操作 （主要是参数检查功能）
若是直接进行属性修改                                   ---快但功能不完全
将属性修改 转成 方法修改 // 将属性调用 改成 方法调用     ---功能完全但慢
@property装饰器就是负责把一个方法变成属性调用的         ---使得属性操作又快又功能完整



实现方法：（把一个属性的构建从__init__分为getter与setter操作）
!!!注意事项!!! ：property后的方法名就是目标属性名！self.xxx 是该方法属性，不是目标属性，也不可以用目标属性名！
 把一个getter方法变成属性，只需要加上@property就可以了，
 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作

 只读属性：只定义getter方法，不定义setter方法就是一个只读属性

 多重继承：
 单继承通过庞大的继承链从而确定继承关系，确定继承的功能
 多继承通过类的组合(Xxxx, YyyyMixIN, ZzzzMixIn),来确定继承关系

定制类：
__iter__():使类返回一个迭代对象 （但不是list 或者 tuple） def __iter__(self): return self
__getitem__():使类变成一个列表
__setitem__()：使类变成一个dict
__delitem__()：
__call__()：使类创建出来的对象可以直接对自己进行方法调用  eg: name_instance()

枚举类：
from enum import Enum
通过成员名和成员值枚举常量，可以把Enum类看作一个字典（具有name 和 value键值对）
                                        （也可进行__members__字典化操作！！！）
Enum类成员不可比较(IntEnum类可以比较)
调用时就好像字典的调用，可以用  Gender["Male"] / Gender(index) 调用常量

type() 1，可以返回一个类型 2，当有变量接收时则可以动态创建一个类（参数：类名 / 继承父类 / dict(方法名 = 已包装方法名)）

"""
from enum import Enum, unique
@unique
class Color(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4

print(Color.red)
member = Color.red
print(member.name + " he " + str(member.value))
for i in Color.__members__.values():
    print(i)
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：


class Gender(Enum):
    Male = 0
    Female = 1


class Students(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

student = Students("MC", Gender["Male"])
print(student.gender)

# ##
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


wyf = Student("wyf")
wyf2 = Student("wyf")
wyf22 = Student("wyf")
print(Student.count)


class Screen(object):
    @property
    def width(self):
        return self.text1

    @width.setter
    def width(self, value):
        # if not isinstance(value, float):
        #     raise ValueError("please input a number!")
        self.text1 = value

    @property
    def height(self):
        return self.text2

    @height.setter
    def height(self, value):
        # if not isinstance(value, float):
        #     raise ValueError("please input a number!")
        self.text2 = value

    @property
    def resolution(self):
        R = self.height * self.width
        return R


screen = Screen()
screen.height = 101
screen.width = 101
print(screen.width)
print(screen.height)




===================================================
#内置函数dir() 的使用，查看对象可以调用的方法  对象-函数数据变量都是一个对象
#下滑线内置方法和属性  __new__ __init__ __del__ __str


 #类的创建和其属性的设置
#所有类创造的一步  -- 需求分析（造句，提词） - 名词-类 形容词（固定/随机）-属性  动词-方法
#面对对象编程的特点---封装 （主程序中只让对象去工作，而不关心具体细节）
#给类添加方法 1，对于不同的对象，代码是相似还是一致 2，对象间是否存在异类调用
#给类增加属性 1，对于不同对象，属性的调用是固定还是随机
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

=======================================
"""

小明爱跑步案例演习
#如果不同对象的方法一致，只是操作的属性不同 ---
#如果不同对象的方法相似但是不完全相同，可使用创建父子类方法重写。

"""
class Person(object):
    def __init__(self, name ,height):
        #记录吃喝次数
        self.count = 0
        self.name = name
        self.height = height


    def run(self):
        self.height -= 0.5
        print("[%s] 进行了一次 [跑步运动]"% self.name)
        print("[%s]的体重 - [0. 5kg],此时体重为 [%f]" % (self.name, self.height))
        self.count += 0.5

    def eat(self):
        self.height += 1.0
        print("[%s] 进行了一次 [吃饭]" % self.name)
        print("[%s]的体重 + [1. 0kg],此时体重为 [%f]" % (self.name, self.height))
        self.count -= 1

    def __del__(self):
        if self.count > 0 :
            print("今天[%s]的减肥计划成功啦！共减下 [%f]"%(self.name, self.count))
        if self.count <= 0:
            print("今天[%s]的减肥计划失败啦！体重增加 [%f]"%(self.name, self.count))

wangyufeng = Person("王雨峰", 75)

====================================================
class House(object):
    def __init__(self):
        self.house_type = "超级无敌海景房"
        self.house_area = 150
        self.house_freearea = 150
        self.houseitem_list = []

    def __str__(self):
        return "房屋的型号为[%s]，总面积有[%.3f],内已置家具[],剩余房屋面积[%.3f]"%(self.house_type, self.house_area, self.house_freearea)

    #方法操作的对象不为本类中的属性
    def add(self, name):
        self.houseitem_list.append(name)


class HouseItem(object):
    def __init__(self, name, area):
        self.name = name
        self.item_area = area

    #将此方法直接设置成家具的方法的直接原因为：家具的面积属性存在于这个家具类之中
    def reduce(self):
        house.house_freearea -= self.item_area




bed = HouseItem("席梦思", 4)
table = HouseItem("沉香木桌",3)
house = House()
house.add(bed.name)
house.add(table.name)
bed.reduce()
table.reduce()
print(house)
=================================================
"""

面对对象复习计划，先面对数学对象，然后才有面对python对象(*^_^*)。
今天的项目规划是   1，整理好数学1-4章ppt中的知识点和定义  1h
 2，重刷一遍题目。  2h
 3，交替看书 - 《计算机》1h《数分》 4h
 4，最后继续面对对象的学习  任意
 # 5,了解一下什么是傅里叶定理
 # 6，制定好下周的计划表，一定要加入适当的科学的英语学习计划

"""
import os

print("hello")
i = os.system("cls")
===============================================
"""

士兵突击案例演练
当对象的属性是一个具体的包含有方法的对象时

需求分析：王雨峰，是一名有枪的士兵，他的枪是ak47 有子弹并且可以进行开枪射击也可以填充弹药
类：人与枪，枪的对象为士兵的属性
属性：人：名字（随机），#配枪（需要调用对象）
     枪：名字（随机），子弹数量

#分析方法时需要考虑到的：调用的属性是否是本类中的？/调用的属性是否是封装有其他方法  参数是别的方法的属性 vs 直接调用一个别的对象的属性
方法1.0：人：填充弹药（子弹的数量），开火射击（子弹的数量） #fire（调用枪射击）
        枪：无

"""



# #尝试一：不进行对象-属性传递  但是直接使用它类对象的属性进行调用                                         ------【不推荐的方式】
# #优劣分析：以现在的知识水平无法做出好而全面的的解释和分析，反正大佬们不这么用你就别这么用（狗头狗头护体）
# class Soilder(object):
#     def __init__(self, soilder_name):
#         self.soilder_name = soilder_name
#         # self.gun = None
#     def fire(self):
#         if gun.bullet_count == 0:
#             print("子弹不足，需要上弹")
#             return
#         gun.bullet_count -= 10
#         print("突" * 10)
#         print("[%s] 的配枪 [%s] 子弹剩余 [%d]\n"%(self.soilder_name, gun.gun_name, gun.bullet_count) )
#
#     def in_bullet(self):
#         gun.bullet_count += 30
#         print("[%s] 的配枪 [%s] 子弹数目 +30 共有[%d]\n"%(self.soilder_name, gun.gun_name,gun.bullet_count))
#
#
# class Gun(object):
#     def __init__(self, gun_name, bullet_count):
#         self.gun_name = gun_name
#         self.bullet_count = bullet_count
#
# gun = Gun("AK47",0)
# wangyufeng =Soilder("王雨峰")
# wangyufeng.in_bullet()
# wangyufeng.fire()

#尝试二：进行对象-属性传递  使用它类对象转化为后调用                                                          ------【Great!】
class Soilder(object):
    def __init__(self, soilder_name):
        self.soilder_name = soilder_name
        self.gun = None
    def fire(self):
        if gun.bullet_count == 0:
            print("子弹不足，需要上弹")
            return
        self.gun.bullet_count -= 10
        print("突" * 10)
        print("[%s] 的配枪 [%s] 子弹剩余 [%d]\n"%(self.soilder_name, self.gun.gun_name, self.gun.bullet_count) )

    def in_bullet(self):
        gun.bullet_count += 30
        print("[%s] 的配枪 [%s] 子弹数目 +30 共有[%d]\n"%(self.soilder_name, self.gun.gun_name, self.gun.bullet_count))


class Gun(object):
    def __init__(self, gun_name, bullet_count):
        self.gun_name = gun_name
        self.bullet_count = bullet_count

gun = Gun("AK47",0)
wangyufeng =Soilder("王雨峰")
wangyufeng.gun = gun
wangyufeng.in_bullet()
wangyufeng.fire()

# #尝试三：两个类之间互不干涉，只在方法中使用形参                                                 ------【不推荐的方式】
# #优劣分析：劣势：不能很好地联系两个类，且若过多调用另一类属性时，方法执行的时候需要每次写入大量的参数
#         #优势：当进行小小的调用时可以选择
# class Soilder(object):
#     def __init__(self, soilder_name):
#         self.soilder_name = soilder_name
#
#     def fire(self, gun_name, bullet_count):
#         if gun.bullet_count == 0:
#             print("子弹不足，需要上弹")
#             return
#         bullet_count -= 10
#         print("突" * 10)
#         print("[%s] 的配枪 [%s] 子弹剩余 [%d]\n"%(self.soilder_name, gun_name, bullet_count) )
#
#     def in_bullet(self, gun_name, bullet_count):
#         gun.bullet_count += 30
#         print("[%s] 的配枪 [%s] 子弹数目 +30 共有[%d]\n"%(self.soilder_name, gun_name, bullet_count))
#
#
# class Gun(object):
#     def __init__(self, gun_name, bullet_count):
#         self.gun_name = gun_name
#         self.bullet_count = bullet_count
#
# gun = Gun("AK47",0)
# wangyufeng =Soilder("王雨峰")
# wangyufeng.in_bullet(gun.gun_name, gun.bullet_count)
# wangyufeng.fire(gun.gun_name, gun.bullet_count)