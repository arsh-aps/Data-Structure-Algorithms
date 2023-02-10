#Reverse
arr = input('Enter something ').split()
def revList(l, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
revList(arr, 0, 3)
print(arr)

#Left rotate and right rotate
arr1 = input('Enter array: ').split()
print('Array entered: ' + str(arr1))
d = int(input('How many spaces do you want to rotate: '))

def lrotate(arr, d):
    return arr[d:] + arr[0:d]

def rrotate(arr, d):
    return arr[d+1:] + arr[0:-d]

print(lrotate(arr1, d))
print(rrotate(arr1, d))

#Search, insert and delete
arr = input('Enter array: ').split()
print('Array entered: ' + str(arr))
elem = int(input('Enter elem to be searched: '))

def searchArray(arr, elem):
    for i in range(len(arr)):
        if elem == int(arr[i]):
            return i
    return 'Can no be found!'
print(searchArray(arr,elem))

def insertArray(arr, position, elem):
    return arr[0:position] + [elem] + arr[position:]

print(insertArray(arr,3,123))
print('Array before deleting: ' + str(arr))
def deleteArray(arr, elem):

    index = searchArray(arr, elem)
    if not isinstance(index, int):
        return 'element not found'
    temp = arr[:index]
    for i in range(index+1, len(arr)):
        temp.append(arr[i])
    return temp

elem = int(input('Enter number to be deleted: '))

print(deleteArray(arr,elem))

#Binary Search
arr = [1, 2, 3, 4, 5]

def binarySearch(arr, low, high, elem):
    mid = int((high + low)/2)
    if elem == arr[mid]:
        return mid
    elif elem < arr[mid]:
        return binarySearch(arr, low, mid-1, elem)
    elif elem > arr[mid]:
        return binarySearch(arr, mid+1, high, elem)
    else:
        return -1

print(binarySearch(arr, 0, len(arr), 3))

#Selection sort
arr = [10,1,5,6,3,2,234,2,21]

for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

print(arr)

#Bubble sort
arr = [10,1,5,6,3,2,234,2,21]
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)