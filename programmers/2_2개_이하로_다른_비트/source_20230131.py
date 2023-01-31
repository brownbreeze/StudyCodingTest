def solution(numbers):
    answer = []
    history = {}
    for number in numbers:
        if number in history:
            answer.append(history[number])
            continue
        b = number
        while True:
            b+=1
            diff = list("{0:b}".format(number^b)).count('1')
            if diff <= 2 :
                break
        answer.append(b)
        history[number] = b
    return answer
