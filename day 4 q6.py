def delchar(s, c):
   
    if len(c) != 1:
        return s
    
    
    result = ""
    
    
    for char in s:
       
        if char != c:
            result += char
    
    return result


s = "hello world"
c = "o"
print(delchar(s, c))  
