def solution(n, times):
    answer = 0
    left, right = 1, max(times)*n
    while left<=right:
        mid = (right+left)//2
        posible_person = sum([mid//time for time in times])
        if posible_person >= n:
            right = mid-1
            answer = mid
        else:
            left = mid+1
    return answer
