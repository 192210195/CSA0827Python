def length_of_last_word(s: str) -> int:
 
    words = s.split()
    
    if not words:
        return 0

    return len(words[-1])

s = "Hello World"
print(length_of_last_word(s)) 
