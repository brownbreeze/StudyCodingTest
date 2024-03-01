import sys
d = dict()
def w(a,b,c):
    name = f'{a},{b},{c}'
    if name in d:
        return d[name]
    if a<=0 or b <=0 or c<= 0:
        d[name] =1 
        return 1
    if a > 20 or b > 20 or c > 20:
        d[name] = w(20,20,20)
        return d[name]
    if a< b and b< c :
        d[name] = w(a,b,c-1) + w(a,b-1,c-1)- w(a,b-1,c)
        return d[name]
    d[name] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return d[name] 

input = sys.stdin.readline
while True :
    arr = input().split()
    if arr[0] == '-1' and arr[1] == '-1' and arr[2] == '-1':break
    vals = w(int(arr[0]),int(arr[1]),int(arr[2]))
    print(f'w({arr[0]}, {arr[1]}, {arr[2]}) = {vals}')

