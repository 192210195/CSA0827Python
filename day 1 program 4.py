x = int(input("Enter the number:"))

if x < 0:  
    is_palindrome = False
else:
    is_palindrome = str(x) == str(x)[::-1]

print(is_palindrome) 
