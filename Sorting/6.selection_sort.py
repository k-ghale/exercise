
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        smallest_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        min_value= nums.pop(smallest_idx)
        nums.insert(i, min_value)
    return nums

# implementation

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

print(selection_sort(mylist))
