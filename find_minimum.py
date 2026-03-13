
import math

def find_minimum(nums):
    minimum = float("inf")
    if len(nums) == 0:
        return None;
    for items in nums:
        if items < minimum:
            minimum = items
    return minimum


# test

nums = [2,3,5,2,4,6,1,63,3]

print(find_minimum(nums))

