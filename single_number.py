
def single_number(nums):
    n = len(nums)
    num = 0
    for n in nums:
        num ^= n

    return num

# implementaion

n = [4,1,2,1,2]
print(single_number(n))

