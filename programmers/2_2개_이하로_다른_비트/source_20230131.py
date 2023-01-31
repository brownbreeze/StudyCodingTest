def solution(numbers):
    answer = []
    history = {}
    for number in numbers:
        if number in history:
            answer.append(history[number])
            continue
        data = "{0:b}".format(number)
        idx = 0 
        for i in data[::-1]:
            idx +=1
            if i == '0' : break
        else:
            idx+=1
        temp = 1 if idx == 1 else pow(2,idx-2)
        answer.append(number+temp)
        history[number] = number+temp
    return answer
