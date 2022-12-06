def solution(line):
    dot_list = set()
    x_range = [0,0]
    y_range = [0,0]
    for l1 in line:
        for l2 in line:
            if l1 == l2: continue
            a,b,e = l1
            c,d,f = l2
            if a*d-b*c == 0 : continue
            x = (b*f-e*d)/(a*d-b*c)
            y = (e*c-a*f)/(a*d-b*c)
            if x != round(x) or y != round(y): continue 
            x = (int)(x)
            y = (int)(y)
            dot_list.add((x,y))
            if len(dot_list)==1:
                x_range[0] = x
                x_range[1] = x
                y_range[0] = y
                y_range[1] = y
                continue
            x_range[0] = x if x < x_range[0] else x_range[0] 
            x_range[1] = x if x > x_range[1] else x_range[1] 
            y_range[0] = y if y < y_range[0] else y_range[0] 
            y_range[1] = y if y > y_range[1] else y_range[1]
    if len(dot_list) == 1: return ["*"]
    y_len = y_range[1]-y_range[0]+1 #if y_range[1]-y_range[0] != 0 else 1
    x_len = x_range[1]-x_range[0]+1 #if x_range[1]-x_range[0] != 0 else 1
    #print(y_len, x_len)
    answer = [["." for _ in range(x_len)] for _ in range(y_len)]
    dot_list = list(dot_list)
    #print(len(answer))
    #print(len(answer[0]))
    for dot in dot_list:
        #print(dot)
        answer[y_range[1]-dot[1]][dot[0]- x_range[0]] = '*'
        #print(f'{(dot[0]- x_range[0])}')
        #print(f'{(y_range[1]-dot[1])}')
    #print(answer)
    final_answer = []
    for line in answer:
        final_answer.append(''.join(line))
    return final_answer
