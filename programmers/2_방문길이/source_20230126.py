def solution(dirs):
    answer = 0
    cur_pos = [0,0]
    dir_pos = [[-1,0,1,0],[0,-1,0,1]] #[0][?] = y, [1][?] = x
    dir_idx = ['D','L','U','R']
    arr = []
    for dir in dirs:
        ch_y = cur_pos[0] + dir_pos[0][dir_idx.index(dir)]
        ch_x = cur_pos[1] + dir_pos[1][dir_idx.index(dir)]
        if ch_y not in range(-5,6) or ch_x not in range(-5, 6): continue
        if ch_y > cur_pos[0] or ch_x > cur_pos[1]:
            arr.append((ch_y,ch_x,cur_pos[0],cur_pos[1]))
        else :
            arr.append((cur_pos[0],cur_pos[1],ch_y,ch_x))
        cur_pos[0] = ch_y
        cur_pos[1] = ch_x
    answer = len(set(arr))
    return answer
