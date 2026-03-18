
def merge_sort(arr, l, r):
    if l < r:
        m = l + (r-l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l , m, r)

def merge(arr, l, m ,  r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l+i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while(i < n1) and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1


# implementation

arr = [12, 11, 13, 5, 6, 7]
print("given array is : ", arr)

# merge sort
merge_sort(arr, 0, len(arr)-1)
print(arr)
