
def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

# implementation

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

print(bubble_sort(mylist))

