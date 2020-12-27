class House():
    def __init__(self,h_free):
        self.kind = "big"
        self.house_square = 150
        self.house_freesquare = h_free
        #不一定所有  不定属性都需要加入形参  ？设想-家具的put行为自动添加？
        self.house_julist = []

    def __str__(self):
        return ("户型：%s 总面积：%d 剩余房间面积：%0.2f 内置家具 %s"
                %(self.kind,self.house_square,
                  self.house_freesquare,self.house_julist))
    def add_ju(self,item):
        print("要添加%s" %item)
        self.house_julist.append(item)
class Ju():
    def __init__(self,ju_name,j_square):
        self.name = ju_name
        self.ju_square = j_square

    def put(self,house):
       house.house_freesquare -= self.ju_square   #曾犯下的错  --要针对 对象 使用属性调用


#---------------------------------------------------------------------------------
house = House(150)

bed = Ju("席梦思",4)
chest = Ju("衣柜",2)

table = Ju("餐桌",1.5)

bed.put(house)
chest.put(house)
table.put(house)
house.add_ju("席梦思")
house.add_ju("衣柜")
house.add_ju("餐桌")


print(house)