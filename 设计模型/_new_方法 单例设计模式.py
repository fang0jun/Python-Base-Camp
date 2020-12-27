class MusicPlayer():

    def __new__(cls, *args, **kwargs):
        #检验呢哇方法是否会被自动调用
        print("hihihii")
        #给对象分配空间
        instance = super().__new__(cls)
        #返回一个对象
        return instance

    def __init__(self):
        print("播放器初始化")

player = MusicPlayer()
print(player)