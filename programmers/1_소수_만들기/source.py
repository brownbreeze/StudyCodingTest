from itertools import combinations, permutations

def solution(nums):
    answer = 0
    
    num_list = [0 for _ in range(3001)]
    combi = list(combinations(nums, 3))
    
    for i in range(2,1501):
        j = 2
        if num_list[i]==1: continue
        while True:
            if i*j > 3000: break
            num_list[i*j] = 1
            j+=1
    # print(num_list[:30])
    
    for val in combi:
        if num_list[sum(val)]==0:
            answer+=1
    return answer
