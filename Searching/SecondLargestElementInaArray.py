


# Second Largest Element in an Array

arr = [1,2,3,4,5,6,7]

us_arr = [112,2345,54756,568758,453,345]


# first method

def search1( arr ):
    arr.sort()
    return arr[len(arr) - 2]

print(search1(arr))
print(search1(us_arr))

# other method

def search2(arr):
    n = len(arr) 
    largest = -1
    secondLargest = - 1

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]


    for i in range(n):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i] 

    return secondLargest

print(search2(arr))
print(search2(us_arr))

# last method

def search3(arr):
    n = len(arr)
    l = -1
    sl = -1

    for i in range(n):
        if arr[i] > l:
            sl = l
            l = arr[i]
        elif arr[i] < l and arr[i] > sl:
            sl = arr[i]
    
    return sl

print(search3(arr))
print(search3(us_arr))


