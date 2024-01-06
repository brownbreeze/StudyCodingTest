def getMyDivisor(n):
    divisorsList = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
    # divisorsList.sort()
    return len(divisorsList)
    
def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        t = getMyDivisor(i)
        if t > limit:
            answer += power
            continue
        answer += t
    return answer
