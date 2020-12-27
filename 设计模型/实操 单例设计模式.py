# class Musicplayer():
#     #设置的对象是只与类有关系的，故设置类属性，以保存该对象
#     num = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.num is None:
#             cls.num = super().__new__(cls)
#             return cls.num
#         else:
#             return cls.num
#
#     def __init__(self, music_name):
#         self.music_name = music_name
#
# music1 = Musicplayer("hongri")
# music2 = Musicplayer("fengyu")
# print(music1)
# print(music2)
class MusicPlayer():
    #设置的对象只与类有关，故设置一个类属性，已保存该对象
    num = None

    def __new__(cls, *args, **kwargs):
        if cls.num is None:
            cls.num = super().__new__(cls)
        return cls.num

    def __init__(self, music_name):
        self.music_name = music_name

music1 = MusicPlayer("sss")
music2 = MusicPlayer("ssss")

print(music1)
print(music2)