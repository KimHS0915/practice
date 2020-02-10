with open('problem11.txt', 'r') as f:
    txt = f.readlines()

arr = []
for t in txt:
    arr.append(list(map(int, t.split())))

h = 0
for i in range(len(arr)):
    for j in range(len(arr)-3):
        tmp = arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3]
        if h < tmp:
            h = tmp

v = 0
for i in range(len(arr)-3):
    for j in range(len(arr)):
        tmp = arr[i][j] * arr[i+1][j] * arr[i+2][j] * arr[i+3][j]
        if v < tmp:
            v = tmp

d = 0
for i in range(len(arr)-3):
    for j in range(len(arr)-3):
        tmp = arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3]
        if d < tmp:
            d = tmp

rd = 0
for i in range(len(arr)-3):
    for j in range(len(arr)-3):            
        tmp = arr[i][j+3] * arr[i+1][j+2] * arr[i+2][j+1] * arr[i+3][j]
        if rd < tmp:
            rd = tmp

answer = max(h, v, d, rd)
print(answer)