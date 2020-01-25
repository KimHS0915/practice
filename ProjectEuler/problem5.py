def gcd(a, b):
    if a < b:
        a, b = b, a
    tmp = a % b
    if tmp == 0:
        return b
    else:
        return gcd(b, tmp)

def lcm(a, b):
    return a*b // gcd(a, b)

def smallest_multiple(n):
    lst = list(range(1, n+1))
    while True:
        x = lst.pop()
        y = lst.pop()
        lst.append(lcm(x, y))
        if len(lst) == 1:
            return lst

answer = smallest_multiple(20)
print(answer)