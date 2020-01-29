def sum_prime(n):
    sieve = [False, False] + [True]*(n - 1)
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i+i::i] = [False]*len(sieve[i+i::i])
    prime_lst = [num for num, bol in enumerate(sieve) if bol]
    return sum(prime_lst)

ans = sum_prime(2000000)
print(ans)