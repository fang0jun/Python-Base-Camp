lst = [4,5,6,3,2,1]
#print(insert_sort(lst))

def insertSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            j -= 1
    return arr
print(insertSort(lst))
