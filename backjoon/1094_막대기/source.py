import sys
def solution(num):
	return str(bin(num)).count('1')

input = sys.stdin.readline
t = int(input())
print(solution(t))

