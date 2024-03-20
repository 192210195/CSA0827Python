def count_ways(n):
    if n == 0 or n == 1:
        return 1

    ways = [0] * (n + 1)

    ways[0], ways[1] = 1, 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    
    return ways[n]

n = int(input("Enter the number of steps: "))
ways = count_ways(n)
print("Number of distinct ways to climb {} steps: {}".format(n, ways))
