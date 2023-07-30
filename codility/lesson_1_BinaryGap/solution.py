# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    b = format(N, 'b')
    flag = 0 
    gap = 0 
    maxgap = 0
    for s in b : 
        if s == '1':
            if flag == 0:
                continue
            maxgap = gap if gap > maxgap else maxgap             
            flag = 0
            gap = 0
        else : # s == 0 
            flag = 1
            gap += 1
    return maxgap
