# largest three in an array

arr = [ 43, 3 , 31 , 12 , 14 , 243 , 45 ]

def LargestThree(arr):
    n = len(arr) - 1
    largest_three = []
    arr.sort()  
    while len(largest_three) != 3:
        largest_three.append(arr[n])
        n -= 1
    largest_three.reverse()
    return largest_three


print(LargestThree(arr))

