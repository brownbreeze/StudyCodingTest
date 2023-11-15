from collections import Counter
def solution(participant, completion):
    # answer = ''
    part = Counter(participant)
    comp = Counter(completion)
    # print(part-comp)
    return list(part-comp)[0]
