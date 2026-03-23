

def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while(swapping):
        swapping=False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
        end -= 1

    return nums

# implementaion

nums = [12,3,45,57,23,56]

print(bubble_sort(nums))
