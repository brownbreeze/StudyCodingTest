max = 1000000
m = [1 for i in range(max+1)]  # 해당 값의 약수의 합 f(x)를 담는 메모

m[1] = 0

for i in range(2, max+1):
    j = 2
    while i * j <= max:  # i*j 값이 최대값이 넘지 않을 때까지
        m[i*j] = 0  # 소수가 아니야
        j += 1


def solution(n):
    for i in range(3, n):
        # print(n, i, n-i)
        if m[i] == 0:
            continue
        if m[n-i] == 0:
            continue
        return f'{n} = {i} + {n-i}'
    return "Goldbach's conjecture is wrong."


divList = list()
while True:
    a = int(input())
    if a == 0:
        break
    divList.append(a)
for i in divList:
    print(solution(i))
