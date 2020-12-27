#类属性 类方法
#对象/实例属性 对象/实例方法  ---调用哪种方法的标准是 方法所访问的属性是怎么样的
#私有属性 私有方法
#静态方法   ---即调用该方法时不访问类属性和对象属性  (不需要创建对象再调用)

class Tool:
    #类属性
    count = 0
    #类方法
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量%d"%cls.count)

    #静态方法
    @staticmethod
    def tools():
        pass

    def __init__(self,name):
        self.name = name
        Tool.count += 1

tooll1 = Tool("gongjuren 1")
tooll2= Tool("gongjuren 2")
tooll3= Tool("gongjuren 3")

#调用类方法
Tool.show_tool_count()
Tool.tools()
