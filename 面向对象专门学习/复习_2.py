class House(object):
    def __init__(self):
        self.house_type = "超级无敌海景房"
        self.house_area = 150
        self.house_freearea = 150
        self.houseitem_list = []

    def __str__(self):
        return "房屋的型号为[%s]，总面积有[%.3f],内已置家具[],剩余房屋面积[%.3f]" % (self.house_type, self.house_area, self.house_freearea)

    # 方法操作的对象不为本类中的属性
    def add(self, name, area):
        self.houseitem_list.append(name)
        self.house_freearea -= area

class HouseItem(object):
    def __init__(self, name, area):
        self.name = name
        self.item_area = area

    # 将此方法直接设置成家具的方法的直接原因为：家具的面积属性存在于这个家具类之中
    # def reduce(self):
    #     house.house_freearea -= self.item_area


bed = HouseItem("席梦思", 4)
table = HouseItem("沉香木桌", 3)
house = House()
house.add(bed.name,bed.item_area)
house.add(table.name,table.item_area)
# bed.reduce()
# table.reduce()
print(house)