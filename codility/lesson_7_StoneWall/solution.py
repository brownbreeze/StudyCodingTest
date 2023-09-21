def solution(H):    
    pre_h = H[0]
    build = [pre_h]
    cnt = 0 
    if len(H) == 1: 
        return 1
    for i in range(1, len(H)):
        h = H[i]
        pre_h = H[i-1]
        if pre_h == h:
            continue  
        if pre_h > h : 
            while True:
                if len(build)==0:
                    break
                if build[-1] > h:
                    cnt+=1
                    build.pop() 
                    continue
                elif build[-1] == h:
                    build.pop()
                break
                
            build.append(h)
            continue 
        build.append(h)
    cnt += len(build)
    return cnt 
