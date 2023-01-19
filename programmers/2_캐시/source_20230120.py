def solution(cacheSize, cities):
    answer = 0
    cnt = [0 for _ in range(cacheSize)]
    arr = ["" for _ in range(cacheSize)]
    total = -1
    city_size = len(cities)
    if cacheSize == 0:
        return 5*len(cities)
    for i in range(city_size):
        cities[i] = cities[i].upper()
        cnt = [c+1 for c in cnt]
        if cities[i] in arr: # 있음
            cnt[arr.index(cities[i])]=0
            answer += 1
            continue
        #없음
        answer += 5
        if "" in arr:
            idx = arr.index("")
            arr[idx] = cities[i]
            cnt[idx] = 0
            continue
        # cnt 가장 높은 값
        idx = cnt.index(max(cnt))
        arr[idx] = cities[i]
        cnt[idx] = 0
        
    return answer
