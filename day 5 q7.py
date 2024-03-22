def longestSubstring(s, k):
    if not s:
        return 0
    
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    
    all_chars_at_least_k = all(count >= k for count in char_count.values())
    if all_chars_at_least_k:
        return len(s)
    
    
    for char, count in char_count.items():
        if count < k:
            return max(longestSubstring(substring, k) for substring in s.split(char))
    
    
    return len(s)


s = "ababbc"
k = 2
print(longestSubstring(s, k))  
