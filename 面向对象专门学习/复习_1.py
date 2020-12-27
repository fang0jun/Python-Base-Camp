#开发步骤-确定好类和 类的属性(特征)和类的方法（行为）
#  ---以上的确定方法---元素提炼法---名词-类  形容词-类的属性  动词-类的方法
"""

小明今年18岁 ， 身高1.78，每天早上去跑步，跑完会去吃东西
小美今年17岁，身高1.65， 喜欢吃东西
名词 - 小明小美 东西
动词 - 跑 吃
形容词 - 男女性别 ， 身高

"""

import random

class Person(object):
    def __init__(self, sex, height):
        self.sex = sex
        self.height = height
        self.number = random.randint(0,6)
        self.diet_list = ["周一餐", "周二餐", "周三餐", "周四餐", "周五餐", "周六餐", "周日餐"]

    def run(self):
        print("慢慢地晨跑")

    def eat(self):
        print("今天吃[{}]".format(self.diet_list[self.number]))


xiaoming = Person("小明", 178)
xiaomei = Person("小美", 165)
xiaoming.run()
xiaoming.eat()
xiaomei.eat()