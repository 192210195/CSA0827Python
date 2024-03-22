def check_divisibility(a, b):
    prod = a * b
    s = a + b

    if prod % s == 0:
        return "YEAH"
    else:
        return "NAH"

# Example usage:
test_cases = [
    (4, 6),
    (10, 5),
    (3, 4)
]

for a, b in test_cases:
    print(check_divisibility(a, b))
