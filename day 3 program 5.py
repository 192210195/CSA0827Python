def min_jumps(nums):
    if not nums:
        return -1
    
    n = len(nums)
    max_reachable = nums[0]
    jumps = 1
    steps = nums[0]
    
    for i in range(1, n):
        if i == n - 1:
            return jumps
        
        max_reachable = max(max_reachable, i + nums[i])
        steps -= 1
        
        if steps == 0:
            jumps += 1
            if i >= max_reachable:
                return -1
            steps = max_reachable - i
            
    return jumps


nums = [2, 3, 1, 1, 4]
print(min_jumps(nums))  
