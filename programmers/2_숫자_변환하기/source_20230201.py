from collections import deque
def go_find(x,y,n):
    li = deque()
    li.append((x,0))
    check = [0 for _ in range(1000000)]
    while True:
        if len(li) == 0: break
        x, cnt = li.popleft()
        
        if x+n == y or x*2 == y or x*3 == y:return cnt+1
        
        if x*3 < y and check[x*3]==0: 
            check[x*3] = 1
            li.append((x * 3, cnt+1))  
        if x*2 < y and check[x*2]==0: 
            check[x*2] = 1
            li.append((x * 2, cnt+1))   
        if x+n < y and check[x+n]==0:
            check[x+n] = 1
            li.append((x + n, cnt+1))   
    return -1
    
def solution(x, y, n):
    if x==y: return 0
    answer = go_find(x,y,n)
    return answer


