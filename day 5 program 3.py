import math

def num_squares(n: int) -> int:
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        min_num_squares = float('inf')
        j = 1
        while j * j <= i:
            min_num_squares = min(min_num_squares, dp[i - j * j] + 1)
            j += 1
        dp[i] = min_num_squares
    
    return dp[n]

# Example usage:
n = 12
print(num_squares(n))  # Output: 3
