def solution(numbers, target):
    answer = 0
    num_len = len(numbers)
    for num in range(1, 1 << num_len):
        temp = 0
        for i in range(num_len):
            if num & (1<<i):
                temp += numbers[i]
            else:
                temp -= numbers[i]
        if temp == target : answer += 1
    return answer
