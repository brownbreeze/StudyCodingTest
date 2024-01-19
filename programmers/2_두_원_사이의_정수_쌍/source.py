def get_dot_cnt_quater(r):
    lcnt = 0
    icnt = 0
    t = r**2
    for y in range(0,r+1):
        for x in range(1,r+1):
            d =y**2+x**2 
            if d <t:
                icnt+=1
            elif d==t:
                lcnt+=1
    return lcnt,icnt

def solution(r1, r2):
    l2,t2=get_dot_cnt_quater(r2)
    l1,t1=get_dot_cnt_quater(r1)    
    return (l2+t2-t1)*4
