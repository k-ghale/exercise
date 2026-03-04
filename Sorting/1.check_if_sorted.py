
#using recursion
def check_sorter_helper(arr, n):
    #base case
    if(n == 0 or n == 1):
        return True
    #check
    return (arr[n-1] >= arr[n-2] and check_sorter_helper(arr,n-1))

def check(arr):
    n = len(arr)
    return check_sorter_helper(arr, n)

if __name__ == "__main__":
    #test
    unsorted_arr = [10,20,3,4,5,6]
    sorted_arr = [10,20,30,40,50,60]

    #print
    print(check(unsorted_arr))
    print(check(sorted_arr))

