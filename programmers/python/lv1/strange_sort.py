def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda word: word[n])