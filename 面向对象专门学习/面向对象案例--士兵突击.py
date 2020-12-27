#类一的属性是类二的对象，类一的属性(None)通过类二的对象赋值                            属性是它类对象  (类)内None外赋
#类一的方法要调用类二的方法时，以属性（等同于类二对象）调用另一类方法                    属性（对象）调方法
#is 身份运算符比较内存地址（即是否同一个对象变量/None）
class Gun():
    def __init__(self,g_model):
        self.model = g_model
        self.bullet_count = 0
    def add_bullet(self,num):
        self.bullet_count += num
    def shoot(self):
        #方法中自动从上往下读
        if self.bullet_count == 0:
            print("bullet no enough!")
            #敲黑板！如果不需要执行 方法中的其他代码用return返回
            return
        # if self.bullet_count >= 0:
        self.bullet_count -= 1
        print("[%s]突突突......[%d]"%(self.model,self.bullet_count))


class Person():
    def __init__(self,p_name):
        self.name = p_name
        #定义了属性，但没有设定值
        self.gun = gun
    def fire(self):

        #判断士兵到底有没有枪
        # if self.gun == None:
        if self.gun is None:
            print("士兵[%s]还没有枪"%self.name)
            return
        #开火喊口号
        print("杀呀")

        #让枪填弹---在一个类中调用另一个类的方法
        #self.gun = gun !!  因为类一的属性是类二的对象，故可以以此属性调用另一类方法
        self.gun.add_bullet(50)
        #让枪发射子弹
        self.gun.shoot()

gun=Gun("AK47")
# gun.add_bullet(50)
# gun.shoot()

bin = Person("binge")
#第一个gun是兵的属性 第二个gun是创建出的对象
bin.gun = gun
bin.fire()

print(bin.gun)

