import math

def binsearch(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) / 2
        mid = math.floor(mid)
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

