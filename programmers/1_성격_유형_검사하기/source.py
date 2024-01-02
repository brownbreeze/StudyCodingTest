def solution(survey, choices):
    answer = ''
    arr = [[0,0] for _ in range(4)]
    datas = {'RT':[0,0], 'TR':[0,1], 'CF':[1,0],'FC':[1,1],'JM':[2,0],'MJ':[2,1], 'AN':[3,0], 'NA':[3,1]}
    val = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    
    l  = len(survey)
    for i in range(l):
        chs = survey[i]
        idx = datas[chs]
        chi = choices[i]
        
        if (chi-4) > 0:
            if idx[1] == 0 :
                arr[idx[0]][1] += chi-4
            else:
                arr[idx[0]][0] += chi-4
        else:
            if idx[1] == 0 :
                arr[idx[0]][0] += 4 - chi
            else:
                arr[idx[0]][1] += 4 - chi
                
    for i in range(4):
        answer += val[i][int(arr[i][0] < arr[i][1])]
                
    return answer
