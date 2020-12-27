"""

对于异常的处理 --- 让错误不影响代码的继续运行，而是先 抛出 异常  ---它将在程序中传递

"""

try:
    num = int(input("请输入一个整数"))
    number = 8 / num

    print(number)

except ValueError:
    print("请老老实实地输入一个整数")
except Exception as result:
    print("未知错误 %s" % result)

else:
    print("执行成功继续向下")
finally:
    print("无论如何我都在")
