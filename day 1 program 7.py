n = 2
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

def generate_strings(length, current_string):
    global count
    if length == 0:
        count += 1
        return
    
    for vowel in vowels:
        if not current_string or current_string[-1] <= vowel:
            generate_strings(length - 1, current_string + vowel)

generate_strings(n, '')

print(count)
