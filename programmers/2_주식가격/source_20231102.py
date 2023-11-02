def solution(prices):
    answer = []
    total_len = len(prices)
    for i in range(total_len):
        for j in range(i+1, total_len):
            if prices[i] > prices[j]: 
                answer.append(j-i)
                break 
        else:
            answer.append(total_len-i-1)
        
    return answer
