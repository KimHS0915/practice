def collatz(n):
    count = 1
    while True:
        if n == 1:
            return count 
        n = n/2 if n % 2 == 0 else 3*n + 1
        count += 1

i = 1
chain = 0
number = 0
dic = {}
while i <= 1000000:
    tmp = collatz(i)
    if tmp > chain:
        chain = tmp
        number = i
    i += 1

print(f'number: {number}, chain: {chain}')
