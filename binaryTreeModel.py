import math

def search(arr, target):

    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) / 2
        mid = math.floor(mid)
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

arr = [-2,3,4,7,8,9,11,13]
target = 11

print(search(arr, target))

# check notes if you have any doubt

