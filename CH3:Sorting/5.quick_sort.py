
def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p-1)
        quick_sort(nums, p+1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low,high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[j]
    return i



# implementation

nums = [12,3,45,57,23,56]
low = 0
high = len(nums) - 1

quick_sort(nums, low, high)

print(nums)
