def solution(nums):
    answer = 0
    total_types = len(list(dict.fromkeys(nums)))
    if total_types > len(nums)//2:
        return len(nums)//2    
    return total_types
