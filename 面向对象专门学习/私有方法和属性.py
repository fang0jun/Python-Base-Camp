 #私有属性，不允许在外部直接访问（不希望公开的属性为私有属性）
# 私有方法不允许在外部直接调用  （不希望公开的方法为私有方法）
# 私有属性只可以在内部方法中访问 或者 通过继承父类公有方法来使用父类的私有方法（超级封装）
# 伪·私有   加个_类名即可调用          eg: women._Women__age//women._Women_screct()

class Women:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def __screct(self):
        print("[%s]女士的年龄是%d"%(self.name,self.__age))


women = Women("meimei",18)
print(women)
