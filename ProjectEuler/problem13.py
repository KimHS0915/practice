with open('problem13.txt', 'r') as f:
    data = f.readlines()

result = 0
for num in data:
    result += int(num)
answer = str(result)[:10]

print(answer)