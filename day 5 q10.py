def reverseWords(s):
    words = s.split()
    
    words.reverse()
    
    return ' '.join(words)


s = "  the sky    is blue   "
print(reverseWords(s)) 
