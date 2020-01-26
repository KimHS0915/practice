def sum_square_difference(n):
    x = sum([i**2 for i in range(1, n+1)])
    y = sum([i for i in range(1, n+1)])**2
    return y-x

print(sum_square_difference(100))