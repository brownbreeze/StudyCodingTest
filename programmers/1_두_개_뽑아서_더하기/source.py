import itertools
def solution(numbers):
    li =  list(itertools.combinations(numbers,2))
    li = set(sum(val) for val in li)
    li = list(li)
    li.sort()
    
    return li
