import sys
def solution(c, arr):
	arr[0].sort()
	arr[1].sort()
	for i in range(c):
		if arr[0][i]!=arr[1][i]:
			print('CHEATER')
			return 0
	print('NOT CHEATER')
	

input = sys.stdin.readline
t = int(input())
questions = []
for i in range(t):
	c = int(input())
	arr = []
	for j in range(2):
		lin = input()
		arr.append(lin.split())
	questions.append([c, arr])

for question in questions:
	solution(question[0], question[1])
