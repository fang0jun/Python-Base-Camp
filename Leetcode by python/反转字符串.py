"""

!!!!!!!!!!!!!!感想： 操作for循环一般只能操作一个变量,  for循环更注重次数
                        while可以很多，while循环更注重结束条件

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

"""

# 法一
def rexerse_1(l):

    x, y = 0, -1
    while(x != len(l) // 2):
        l[x], l[y] = l[y], l[x]
        x += 1  # [1,2,3,4,5,6] 2/-3 x = 3  # [1,2,3,4,5,6,7] x = 3
        y -= 1
    return l

list = [1,2,3,4,5,6,7]
print(rexerse_1(list))

# 法二  在原有的列表中操作
def reverse_1(r):

    # 改进
    x, y = 0, -1
    for i in range(len(r) // 2):
        r[x], r[y] = r[y], r[x]
        x += 1
        y -= 1
    return r

print(reverse_1(["h","a","n","n","a","H", "1"]))


# 法二 创建新的列表以操作
def reverse_2(ll):
    ll[0:] = ll[::-1]
    # return ll[0:]
    return ll
print(reverse_2([1,2,3,4,5,7,8,9]))


#   x = r[0]
    # r[0] = r[-1]
    # r[-1] = x
    # for i in range(1, 3):
    #     # r[i],r[-i] = r[-i], r[i]
    #     l = r[i]
    #     r[i] = r[-i - 1]
    #     r[-i - 1] = l
