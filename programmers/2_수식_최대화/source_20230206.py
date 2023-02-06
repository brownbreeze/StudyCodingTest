import re
import itertools
from collections import deque

def solution(expression):
    answer = 0
    expression_list = []
    giho_list = []
    
    flag = 0
    for e in expression:
        if flag == 0 : 
            expression_list.append(e)
            flag = 1
            continue
        if e in ['+','-','*']:
            flag = 0
            expression_list.append(e)
            giho_list.append(e)
            continue
        expression_list[-1]+=e
    
#    expression_list = deque(expression_list)
    all_giho = list(set(giho_list))
    permutations = itertools.permutations(all_giho, len(all_giho))
    for permutation in permutations:
        # print(permutation)
        expression_temp = [int(i) if i not in ['+','-','*'] else i for i in expression_list]
        for do_ex in permutation:
            temp = deque(maxlen=100)
            for i in range(len(expression_temp)):
                cur = expression_temp[i]
                if cur in ['+','-','*']:
                    temp.append(cur)
                    continue
                if i ==0 : 
                    temp.append(cur)
                    continue
                if temp[-1] == do_ex:
                    temp.pop()
                    if do_ex == '+' :
                        temp.append(temp.pop()+cur)
                    elif do_ex == '-':
                        temp.append(temp.pop()-cur)
                    else:
                        temp.append(temp.pop()*cur)
                    continue
                temp.append(cur)
            expression_temp = temp.copy()
        answer = max(answer, abs(temp[0]))
    return answer
