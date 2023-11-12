from collections import Counter
def solution(input_string):
    answer = []
    i = 0
    pre_s = 'A'
    first = ord('a')
    check_list = [0 for _ in range(27)]
    for s in input_string:
        if i == 0 : 
            pre_s = s
            i+=1 
            check_list[ord(s)-first] += 1
            continue
            
        if pre_s == s:
            check_list[ord(s)-first] += 1
        else:
            if check_list[ord(s)-first] != 0 :
                answer.append(s)
                check_list[ord(s)-first]+=1
            else:
                check_list[ord(s)-first]+=1
        pre_s = s 
        i+=1
    if len(answer) == 0 :
        return 'N'
    return ''.join(sorted(list(set(answer))))
