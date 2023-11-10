def solution(sizes):
    answer = 1000000
    size_len = len(sizes)
    temp = 0 
    for i in range(0, 1<<size_len-1):
        h = 0
        w = 0
        for num in range(size_len):
            if i & (1<<num):
                h = h if h > sizes[num][0] else sizes[num][0]
                w = w if w > sizes[num][1] else sizes[num][1]
            else:
                h = h if h > sizes[num][1] else sizes[num][1]
                w = w if w > sizes[num][0] else sizes[num][0]
        temp = h*w
        # print(temp)
        answer = answer if temp > answer else temp         
    return answer
