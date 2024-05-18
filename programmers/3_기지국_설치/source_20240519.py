import math
def solution(n, stations, w):
    answer = 0
    i = 0 
    wl = w*2+1

    for station in stations:
        s = station - w
        e = station + w 
        l = s-1-i
        c = math.ceil(l/wl)
        # print(i,s,e,l,c,   i+c*wl)
        answer += c
        i = e if i+c*wl < e else i+c*wl
    else:
        if i < n:        
            l = n-1-i
            # print(i,s,e,l)
            answer += math.ceil(l/wl)
    return answer
