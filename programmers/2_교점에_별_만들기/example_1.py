def getIntersection(line1,line2):
    A,B,E = line1
    C,D,F = line2
    if A*D - B*C == 0:
        return (None,None)
    return ((B*F-E*D)/(A*D-B*C), (E*C-A*F)/(A*D-B*C))
def isInteger(x,y):
    return x != None and int(x) == x and int(y) == y
def minXY(idx,lst):
    return int(min(lst,key=lambda x: x[idx])[idx])
def maxXY(idx,lst):
    return int(max(lst,key=lambda x: x[idx])[idx])
def solution(lines):
    answer = []
    intersections = set()
    n = len(lines)
    for idx1 in range(n):
        for idx2 in range(idx1+1,n):
            x,y = getIntersection(lines[idx1],lines[idx2])
            if isInteger(x,y):
                intersections.add((y,x))
    for x in range(maxXY(0,intersections),minXY(0,intersections)-1,-1):
        tmp = ""
        for y in range(minXY(1,intersections),maxXY(1,intersections)+1):
            tmp += "*" if (x,y) in intersections else "."
        answer.append(tmp)

    return answer

