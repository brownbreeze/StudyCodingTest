import sys


def solution(num, arr):
    dl = list()
    for i in range(num):
        dl.append([arr[i]/(i+1), i+1, arr[i]])

    dl.sort(key=lambda x: (x[0], x[1]), reverse=True)
    print(dl)
    nmg = num
    mock = 0
    i = 0
    result = 0
    while True:
        print(i, nmg, dl[i][1], result)
        if nmg == 0:
            break
        if i >= num:
            return False
        if nmg // dl[i][1] > 0:
            mock = nmg // dl[i][1]
            result += (mock * dl[i][2])
            nmg = num % dl[i][1]
            i = 0
        else:
            i += 1
    return result


input = sys.stdin.readline
t = int(input())
arr = list(map(int, input().split()))
print(int(solution(t, arr)))
