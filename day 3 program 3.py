def num_identical_pairs(nums):
   
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    
   
    good_pairs_count = 0
    for count in num_counts.values():
        if count > 1:
            good_pairs_count += count * (count - 1) // 2
    
    return good_pairs_count

nums = [1, 2, 3, 1, 1, 3]
print(num_identical_pairs(nums)) 
