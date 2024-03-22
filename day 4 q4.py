def isPalindrome(s):

    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned_string == cleaned_string[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  
