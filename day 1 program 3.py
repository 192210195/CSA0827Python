n = int(input("Enter the number:"))

def get_next(num):
    next_num = 0
    while num > 0:
        digit = num % 10
        next_num += digit ** 2
        num //= 10
    return next_num

seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = get_next(n)

is_happy = n == 1
print(is_happy) 
