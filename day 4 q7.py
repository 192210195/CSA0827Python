def countSortedVowelStrings(n):
    
    dp = [1] * 5      
   
    for i in range(2, n + 1):
        
        for j in range(1, 5):
            dp[j] += dp[j - 1]
    
    
    return sum(dp)


n = 2

print(countSortedVowelStrings(n)) 
