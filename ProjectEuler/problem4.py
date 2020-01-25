def largest_palindrome(n):
    answer = [0,]
    for i in range(1, n):
        for j in range(1, n):
            if str(i*j) == str(i*j)[::-1] and i*j > answer[0]:
                answer = [i*j, i, j]
    return answer

print(largest_palindrome(1000))