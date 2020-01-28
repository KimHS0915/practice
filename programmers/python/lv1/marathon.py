import collections

def solution(participant, completion):
    x =  collections.Counter(participant) - collections.Counter(completion)
    return list(x)[0]