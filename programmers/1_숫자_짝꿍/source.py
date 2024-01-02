def solution(X, Y):
    answer = ''
    Xarr = []
    Yarr = []
    intersec = []

    for x in X:
        Xarr.append(x)
    for y in Y:
        Yarr.append(y)
    Xarr.sort(reverse=True)
    Yarr.sort(reverse=True)
    
    i = 0
    j = 0
    while True:
        if i >= len(Xarr) : break
        if j >= len(Yarr) : break
        if Xarr[i] == Yarr[j]:
            intersec.append(Xarr[i])
            i +=1 
            j +=1
        elif Xarr[i] > Yarr[j]:
            i+=1
        else:
            j+=1
    if len(intersec) == 0 :
        return "-1"
    if set(intersec) == {"0"}:
        return "0"
    return ''.join(intersec)

