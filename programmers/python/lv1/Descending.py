def solution(n):
    lst = sorted(str(n), reverse=True)
    answer = ''
    for i in lst:
        answer += i
    return int(answer)