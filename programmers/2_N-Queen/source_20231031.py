def solution(n):
    answer = 0
    row = [0 for _ in range(n)]
    

    
    def Queen(cnt):
        nonlocal answer
        
        
        if cnt == n : 
            answer += 1
            return 
        else:
            for x in range(n):
                if n%2 == 0 and row[0] >= n//2: break
                row[cnt] = x
                for y in range(cnt):

                    if row[y] == x or abs((x - row[y])/(cnt - y))== 1:
                        break
                else:
                    Queen(cnt+1)
                    
    Queen(0)
    return answer * 2 if n%2 == 0 and n >= 4 else answer 
