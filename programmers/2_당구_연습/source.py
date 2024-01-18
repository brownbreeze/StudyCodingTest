import math
def third_point(i,rowcnt, colcnt, x,y):
    if i==0:
        return x, abs(rowcnt-y)*2+y
    elif i==1:
        return x, -1*y
    elif i==2:
        return abs(colcnt-x)*2+x,y
    else:
        return x*-1,y
    
def get_distance(colcnt,rowcnt,x,y,ball):
    value=math.inf
    bx=ball[0]
    by=ball[1]
    for i in range(4):
        nx,ny = third_point(i,rowcnt,colcnt,bx,by)       
        if nx==x and by in range(min(ny,y),max(y,ny)):
            continue
        elif ny==y and bx in range(min(nx,x),max(nx,x)):
            continue
        value = min(value,abs(nx-x)**2+abs(ny-y)**2)
    return value
    
def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        answer.append(get_distance(m,n,startX, startY, ball))
    return answer
