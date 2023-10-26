def solution(numbers, target):
    answer = 0
    len_num = len(numbers)
    for n in range(1, 1 << len_num):
        temp = 0 
        for i in range(len_num):
            if n & (1<<i):
                temp -= numbers[i]
            else:
                temp += numbers[i]
        if temp == target:
            answer +=1
    return answer
