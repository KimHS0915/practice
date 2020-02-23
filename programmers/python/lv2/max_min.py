def solution(s):
    int_list = list(map(int, s.split()))
    return f'{min(int_list)} {max(int_list)}'