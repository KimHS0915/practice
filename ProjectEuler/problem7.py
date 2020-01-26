def is_prime(n):
    n = abs(n)
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def n_prime(n):
    count = 0
    i = 2
    while True:
        if is_prime(i):
            count += 1
        if count == n:
            return i
        i += 1

answer = n_prime(10001)
print(answer)