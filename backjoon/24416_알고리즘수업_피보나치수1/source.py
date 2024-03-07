import sys
def fib(n):
	n1 = 1
	n2 = 1
	for i in range(2, n):
		t = n2
		n2 += n1
		n1 = t
	return n2 

def solution(num):
	c1 = fib(num)
	print(c1, num-2)

input = sys.stdin.readline
t = int(input())
solution(t)