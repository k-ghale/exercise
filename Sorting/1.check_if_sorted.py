
arr = [10,20,3,4,5,6]

#using recursion
def check_sort_helper(arr, n):
    if (n == 0 or n ==1):
        return True
    
    return (arr[n-1] >= arr[n-2] and check_sort_helper(arr, n-1))

def check_sort(arr):
    n = len(arr)
    return check_sort_helper(arr, n)



print(check_sort(arr))

