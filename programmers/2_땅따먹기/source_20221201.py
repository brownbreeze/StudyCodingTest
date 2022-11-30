def solution(land):
    row_size = len(land)
    fake_land = [list() for _ in range(row_size)]
    
    for r in range(row_size):
        if r==0: 
            fake_land[0] = land[0][:]
            continue
        for c in range(4):
            temp = fake_land[r-1][:]
            temp.pop(c)
            fake_land[r].append( land[r][c] + max(temp) )   
    answer=max(fake_land[-1])
    return answer
