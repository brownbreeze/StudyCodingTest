from itertools import combinations 
import math
def solution(nums):
    answer = 0
    a = list(combinations(nums,len(nums)//2))
    for test in a:
        if len(list(dict.fromkeys(list(test)))) > answer:
            answer =  len(list(dict.fromkeys(list(test))))
    return answer
