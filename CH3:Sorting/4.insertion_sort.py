
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1
    return nums

# implementaion

nums = [12,3,45,57,23,56]

print(insertion_sort(nums));
