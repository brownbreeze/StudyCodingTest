import sys
input = sys.stdin.readline
arr = list(map(int, input().split()))
arr.sort()
for s in arr:
    print(s, end=' ')
