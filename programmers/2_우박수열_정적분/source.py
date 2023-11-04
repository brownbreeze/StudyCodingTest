def solution(k, ranges):
    i = 0 
    num = k
    answer = []
    values = []
    
    arr = list()
    arr.append([i, k])
    
    while True:
        if k <= 1: break
        if k % 2 == 1:
            k = k*3 +1 
        else:
            k /= 2
        i+=1
        arr.append([i, k])
    cnt = i
    for i in range(cnt):
        min_y = arr[i][1] if arr[i][1] < arr[i+1][1] else arr[i+1][1]
        max_y =  arr[i+1][1] if arr[i][1] < arr[i+1][1] else arr[i][1]
        values.append((max_y-min_y)/2+min_y)
    # print(values)
    
    i+=1
    for a,b in ranges:
        a = a
        b = i + b
        temp = sum(values[a:b]) if a <= b else -1
        answer.append(temp)
    return answer
