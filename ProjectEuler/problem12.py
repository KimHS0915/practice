def triangular_number(n):
    return int((n+1)*(n/2))

def divisor(n):
    count = 0
    if n == 1:
        return 1
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            count += 2
    return count

def problem12(n):
    i = 1
    while True:
        t_num = triangular_number(i)
        if divisor(t_num) > n:
            return t_num
        i += 1

answer = problem12(500)
print(answer)
