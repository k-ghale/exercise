
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = (low+high)//2

        if mid == target:
            return True
        
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
    return False

arr = [12,32,1,243,4]

print(binary_search(243, arr))