def generate_pascals_triangle(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i][j] = 1
            else:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

def sum_of_nth_row_in_pascals_triangle(n):
    if n < 0:
        return 0
    row = generate_pascals_triangle(n + 1)[n]  
    return sum(row)


n = 5
print("Pascal's Triangle up to the {}th row:".format(n))
for row in generate_pascals_triangle(n):
    print(row)
print("Sum of elements in the {}th row:".format(n), sum_of_nth_row_in_pascals_triangle(n))
