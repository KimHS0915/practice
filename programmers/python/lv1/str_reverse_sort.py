def solution(s):
    answer = ''
    lst = sorted(s, reverse=True)
    for i in lst:
        answer += i
    return answer