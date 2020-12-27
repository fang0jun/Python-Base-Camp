"""

散列表（字典）的主要应用场景
1，查找
2，防重（缓存）

"""
# 投票
# 将可变数据类型放入方法中将不会储存改变（方法执行完成以后所有程序释放）
dict_1 = {}
def vote(name):
    if name in dict_1.keys():
        print("go away")
    else:
        dict_1[name] = name
        print("ok")
    return dict_1


vote("anna")
print(vote("anna"))
vote("anna")
dict_2 = {}

