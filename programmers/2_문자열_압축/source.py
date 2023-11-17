def solution(s):
    s_len = len(s)
    answer = s_len
    for c in range(s_len//2,0,-1):
        new_len = s_len
        prev_s = ''
        total_str = ''
        cnt = 0 
        for j in range(0, len(s), c):
            if j+c > s_len: 
                total_str += s[j:]
                break
            if len(prev_s) == 0 :
                prev_s = s[j:j+c]
                continue
            if s[j:j+c] == prev_s:
                if cnt == 0:
                    cnt = 2
                elif cnt > 1:
                    cnt += 1 
            else:
                total_str += prev_s
                if cnt != 0:
                    total_str += str(cnt)
                cnt = 0
                prev_s = s[j:j+c]
        if cnt != 0:
            total_str += str(cnt)
        total_str += prev_s
        answer = min(answer, len(total_str))
    return answer
