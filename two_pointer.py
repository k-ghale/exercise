
# num = [1,2,3,4,5,6,7], target = 4, result = [0, 2]
#two pointer approach

def two_pointer(nums, target):
    right = len(nums) - 1
    left = 0

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right-=1

    return -1

if __name__ == "__main__":
    nums  = [1,2,3,4,5,6]
    target = 4

    print(two_pointer(nums,target))


