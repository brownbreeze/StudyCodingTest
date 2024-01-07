def solution(k, score):
    answer = []
    my_li = []
    for i in range(len(score)):
        if len(my_li) < k:
            my_li.append(score[i])
            my_li.sort(reverse=True)
        elif my_li[-1] < score[i]:
            my_li.pop()
            my_li.append(score[i])
            my_li.sort(reverse=True)
        answer.append(my_li[-1])
        
    return answer
