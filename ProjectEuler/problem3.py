def prime_factorization(n):
    i = 2
    lst = []
    while n != 1:
        if n % i == 0:
            lst.append(i)
            n //= i
        else:
            i += 1
    return lst

x = prime_factorization(600851475143)
print(max(x))