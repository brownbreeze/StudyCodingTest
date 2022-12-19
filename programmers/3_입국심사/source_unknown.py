def solution(n, times):
    left , right = 1, max(times)*n
    while left <= right:
        mid = (left+right) // 2 
        people = 0
        # mid 분 이내에 N명 수행이 가능한지 확인 
        for time in times:
            people += mid // time
            if people >= n : 
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else : 
            left = mid + 1
    return answer
