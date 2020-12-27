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
