def is_mirror_number(number):
    reversed_number = number[::-1]  
    return number == reversed_number  


number = input("Enter a number: ")
if is_mirror_number(number):
    print("Yes, the number can be reversed to become a mirror number.")
else:
    print("No, the number cannot be reversed to become a mirror number.")
