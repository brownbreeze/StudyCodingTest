from collections import Counter 

def solution(participant, completion):
    keys = list((Counter(participant)-Counter(completion)).keys())
    return keys[0]
