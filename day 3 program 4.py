def add_binary(a, b):
 
    result = ''
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
       
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
      
        current_sum = digit_a + digit_b + carry
        carry = current_sum // 2
        current_sum %= 2
        
        
        result = str(current_sum) + result
        
   
        i -= 1
        j -= 1
    
    return result


a = "11"
b = "1"
print(add_binary(a, b)) 
