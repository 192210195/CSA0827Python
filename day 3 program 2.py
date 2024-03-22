from itertools import combinations

def find_combinations(digits):
   
    digits_list = [int(digit) for digit in digits]
    
    all_combinations = []
    for r in range(1, len(digits_list) + 1):
        all_combinations.extend(combinations(digits_list, r))
    
    return all_combinations

digits = input("Enter 3 digits separated by spaces: ").split()
if len(digits) != 3:
    print("Please enter exactly 3 digits.")
else:
    combinations = find_combinations(digits)
    print("All possible combinations of team members:")
    for combo in combinations:
        print(combo)
