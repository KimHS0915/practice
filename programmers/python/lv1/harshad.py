def solution(x):
    num_list = [int(str(x)[i]) for i in range(len(str(x)))]
    return x % sum(num_list) == 0