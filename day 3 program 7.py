def permute_unique(nums):
    def backtrack(remaining, permutation):
        if len(permutation) == len(nums):
            permutations.append(permutation[:])
            return

        for i in range(len(remaining)):
            if i > 0 and remaining[i] == remaining[i - 1]:
                continue  
            permutation.append(remaining[i])
            backtrack(remaining[:i] + remaining[i + 1:], permutation)
            permutation.pop()

    nums.sort()  
    permutations = []
    backtrack(nums, [])
    return permutations

nums = [1, 1, 2]
print(permute_unique(nums))
