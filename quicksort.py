

import math

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        i+=1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p+1, high)

# implementation

arr = [12,31,42,45,41,76,87,48]

quick_sort(arr, 0, len(arr) - 1)
print(arr)


print(quick_sort(arr, 0, len(arr) - 1))
