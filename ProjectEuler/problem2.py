i = 1
lst = []
x, y = 1, 0
while True:
    x, y = y, x + y
    if y % 2 == 0:
        lst.append(y)
    if y > 4000000:
        break
print(sum(lst))