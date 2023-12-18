# def get_yacksoo(n):
#     divisorsList = []
#     for i in range(1, int(n**(1/2)) + 1):
#         if (n % i == 0):
#             divisorsList.append(i) 
#             if ( (i**2) != n) : 
#                 divisorsList.append(n // i)

#     divisorsList.sort()
#     return divisorsList

def solution(n, m):
    answer = []
    # n_list = get_yacksoo(n)
    # m_list = get_yacksoo(m)
#     intersection = list(set(n_list) & set(m_list))
#     answer.append(intersection[-1])
    
    i = 0
    for i in range(min(n,m), 0, -1):
        if n%i ==0 and m%i == 0 :
            break
    answer.append(i)
    
    i = 0
    for i in range(max(n, m), n*m+1):
        if i%n == 0 and i%m==0:
            break
    answer.append(i)    
    return answer
