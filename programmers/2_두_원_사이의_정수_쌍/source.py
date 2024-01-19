def get_dot_cnt_quater(r):
    lcnt = 1
    icnt = r-1
    y=r
    x=0
    line=r**2
    while x!=r:
        x+=1
        t=x**2
        while y:
            if t+y**2<=line:
                if t+y**2==line:
                    lcnt+=1
                    icnt-=1
                break
            else:
                y=y-1      
        
        icnt+=(y)
    return lcnt,icnt

def solution(r1, r2):
    l2,t2=get_dot_cnt_quater(r2)
    l1,t1=get_dot_cnt_quater(r1)    
    return (l2+t2-t1)*4
