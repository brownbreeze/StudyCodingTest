def solution(friends, gifts):
    answer = 0
    fl = len(friends)
    fd = {}
    i = 0
    arr = [[0 for _ in range(fl)] for _ in range(fl)]
    rst = [0 for _ in range(fl)]

    for f in friends:
        fd[f] = 0

    for gift in gifts:
        values = gift.split(' ')
        fd[values[0]] +=1
        fd[values[1]] -=1
        arr[friends.index(values[0])][friends.index(values[1])] += 1
    
    for f1 in friends:
        for f2 in friends:
            if f1 <= f2 : continue
            if1 = friends.index(f1)
            if2 = friends.index(f2)
            
            if arr[if1][if2] > arr[if2][if1]:
                rst[if1] += 1
                continue
            elif arr[if1][if2] < arr[if2][if1]:
                rst[if2] += 1
                continue
            if fd[f1] > fd[f2] :
                rst[if1] += 1
            elif fd[f1] < fd[f2]:
                rst[if2] += 1
               
    return max(rst)
