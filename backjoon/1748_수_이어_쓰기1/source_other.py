import sys
input = sys.stdin.readline
n = int(input())
x = len(str(n))
length = 0
cnt = 0
while x > length + 1:
    cnt += 9 * pow(10, length) * (length + 1)
    length += 1
cnt += (n - pow(10, x - 1) + 1) * x
print(cnt)
