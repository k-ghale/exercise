
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right= merge_sort(nums[mid:])
    return merge(left, right)

def merge(first, second):
    result = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i+=1
        else:
            result.append(second[j])
            j+=1

    while i < len(first):
        result.append(first[i])
        i+=1

    while j < len(second):
        result.append(second[j])
        j+=1

    return result

# implementation

nums = [12,3,45,57,23,56]
print(merge_sort(nums))
