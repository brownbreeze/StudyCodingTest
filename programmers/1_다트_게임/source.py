import math
def solution(dartResult):
    answer = 0
    point_list = []
    option_list = [0 for _ in range(3)]
    pos = 0
    bns_opt = 0
    num = 0
    bonus_list = ['S', 'D', 'T']
    for i in range(len(dartResult)):
        if bns_opt :
            bns_opt = 0 
            if dartResult[i] in ['*','#']:
                if dartResult[i] == '*':
                    option_list[pos] = 2
                    if pos >=1: 
                        option_list[pos-1] *= 2
                else:# #
                    option_list[pos] = -1
            else:
                option_list[pos] = 1
            pos +=1
        if dartResult[i] in bonus_list:
            bns_opt = 1
            num = math.pow(num, bonus_list.index(dartResult[i])+1) 
            # print(num, bonus_list.index(dartResult[i]))
            num = num
            point_list.append(num)
            num = 0 
        elif dartResult[i] in '0123456789' :
            if dartResult[i] == '0':
                if num == 1:
                    num = 10
                else:
                    num = 0
            else:
                num = int(dartResult[i])
    else:
        if option_list[-1] == 0:
            option_list[-1] = 1
    
    for p, o in zip(point_list, option_list):
        answer += p*o
                
    # print(point_list)
    # print(option_list)
    return answer
