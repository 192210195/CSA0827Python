def minJumps(nums):
    n = len(nums)
    jumps = [float('inf')] * n
    jumps[0] = 0
    
    for i in range(1, n):
        for j in range(i):
            if j + nums[j] >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    
    return jumps[-1] if jumps[-1] != float('inf') else -1


nums = [2, 3, 1, 1, 4]
print(minJumps(nums))  

