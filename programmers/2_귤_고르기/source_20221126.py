def solution(k, tangerine):
    answer = 0
    dictionary = dict.fromkeys(tangerine,0)
    for tan in tangerine:
        dictionary[tan] = dictionary[tan] + 1 
    sorted_datas = sorted(dictionary.items(), key=lambda d:d[1], reverse=True)
    for _,v in sorted_datas:
        k = k-v
        answer = answer + 1
        if k <=0 :
            return answer
    return answer
