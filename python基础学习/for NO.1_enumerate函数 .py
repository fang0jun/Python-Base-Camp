"""

1,enumerate函数的使用---列举
 enumerate(可遍历数据对象 , start=开始下标)
 返回一个可遍历的数据对象索引序列(元组) , 同时列出数据和数据下标,常常与for一起使用

2,list()方法的使用
 将一个(元组)转化为列表

3,字典get函数
 get(key)
 以键找值，如果值不在字典中返回默认值

4,count()方法
str.count(sub, start= 0,end=len(string)) 默认开头与结尾
string 中 某字符 的次数

5,index()方法
str.index(str, beg=0, end=len(string)) 默认开头与结尾
如果包含子字符串返回开始的索引值，否则抛出异常。

"""

season = ["spring", "summer", "autumn", "winter"]
list_experience = ("spring", "summer", "autumn", "winter")
dictionary = {"one":2, "two":4, "three":9}
print("%d" % dictionary.get("two"))
#使用enumerate返回一个元组 , 同时包含数据与下标
list_1 = list(enumerate(season, start=1))
list_2 = list(list_experience)
print(list_1)
print(list_2)