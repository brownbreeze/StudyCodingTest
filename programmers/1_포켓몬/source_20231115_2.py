def solution(nums):
    data_len = len(set(nums))
    if data_len > len(nums)//2:
        return len(nums)//2
    return data_len

