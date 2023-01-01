def solution(numbers, target):
    answer = 0
    num_len = len(numbers)
    for i in range(1, 1 << num_len):
        temp = 0 
        for num in range(num_len):
            if i & (1<< num) : 
                temp += numbers[num]
            else : 
                temp -= numbers[num]
        if temp == target : answer +=1
    return answer
