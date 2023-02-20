def solution(numbers):
    answer = []
    num_len = len(numbers)
    for i in range(num_len-1):
        j = i+1
        while True:
            if j >= num_len :
                answer.append(-1)
                break
            if numbers[j] > numbers[i]:
                answer.append(numbers[j])
                break
            j+=1
    answer.append(-1)
    return answer
