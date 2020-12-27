"""

士兵突击案例演练
当对象的属性是一个具体的包含有方法的对象时

需求分析：铁憨憨王雨峰，是一名有枪的士兵，他的枪是ak47 有子弹并且可以进行开枪射击也可以填充弹药
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
# wangyufeng =Soilder("铁憨憨王雨峰")
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
        print("[铁憨憨%s] 的配枪 [铁%s] 子弹数目 +30 共有[%d]\n"%(self.soilder_name, self.gun.gun_name, self.gun.bullet_count))


class Gun(object):
    def __init__(self, gun_name, bullet_count):
        self.gun_name = gun_name
        self.bullet_count = bullet_count

gun = Gun("AK47",0)
wangyufeng =Soilder("铁憨憨王雨峰")
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
# wangyufeng =Soilder("铁憨憨王雨峰")
# wangyufeng.in_bullet(gun.gun_name, gun.bullet_count)
# wangyufeng.fire(gun.gun_name, gun.bullet_count)