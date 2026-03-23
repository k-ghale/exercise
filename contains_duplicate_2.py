def containsNearbyDuplicate(nums, k):
    seen = set()
    
    for i in range(len(nums)):
        # Check if duplicate exists in window
        if nums[i] in seen:
            return True
        
        seen.add(nums[i])
        
        # Maintain window size k
        if len(seen) > k:
            seen.remove(nums[i - k])
    
    return False