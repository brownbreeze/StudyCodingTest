def solution(s):
    answer = 0
    x = s[0]
    x_cnt = 1
    nx_cnt = 0
    new_x_flag = False
    for i in range(1,len(s)):
        # print(new_x_flag, answer, x, s[i], x_cnt, nx_cnt)
        if new_x_flag:
            x = s[i]
            x_cnt += 1 
            answer += 1 
            new_x_flag = False
            continue
        if s[i] == x:
            x_cnt +=1 
        else:
            nx_cnt +=1
        if x_cnt == nx_cnt :
            new_x_flag = True
            x_cnt = 0
            nx_cnt = 0
            continue
    else:
        if x_cnt != 0 or nx_cnt != 0:
            # print('!!')
            answer +=1 
        elif new_x_flag:
            answer +=1
        
    return answer
