from itertools import combinations
def solution(nums):
    # answer = 0
    data = combinations(nums, len(nums)//2)
    answer = [len(set(a)) for a in list(data)]
    return max(answer)
