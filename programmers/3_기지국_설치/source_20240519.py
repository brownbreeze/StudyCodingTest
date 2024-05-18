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
        answer += c
        i = e
    else:
        if i < n:        
            l = n-i
            answer += math.ceil(l/wl)
    return answer
