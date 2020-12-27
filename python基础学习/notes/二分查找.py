#二分查找

def twocut(item, arr):
    up = len(arr) - 1
    low = 0
    while up >= low:
        mid = (up + low) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            up = mid - 1
        else:
            low = mid + 1
    return None

print(twocut(4, [1,2,3,4,5,6,7,8,9]))

#选择排序
def findSmall(arr):
    small = arr[0]
    small_index = 0
    for i in range(len(arr)):
        if small > arr[i]:
            small = arr[i]
            small_index = i
    return small_index

def seletion(arr):
    newArr = []
    while arr:
        small_index = findSmall(arr)
        newArr.append(arr.pop(small_index))
    return newArr

print(seletion([1,2,4,7567,223,7,88,2,4,89]))

#递归入门
def countdown(i):
    if i == 0:
        print("0")
    else:
        print(i)
        countdown(i - 1)

countdown(3)

def faxt(i):
    if i == 1:
        return 1
    else:
        result = i * faxt(i - 1)
        return result

print(faxt(5))

def sum(arr):
    i = 0
    if len(arr):
        return arr[0] + sum(arr[1:])
    else:
        return 0

print(sum([1,2,3]))

#快速排序
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([213,52,645,23,756,8,4,22,674,]))

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def twocut(item, arr):
    up = len(arr) - 1
    low = 0
    for i in range(len(arr)):
        mid = (up + low) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            up = mid - 1
        else:
            low = mid + 1
    return None

print(twocut(89,[8,89,241,432,6,6,889,7,78]))
