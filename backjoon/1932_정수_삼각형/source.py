import sys
def solution(n, m):	
	val = []
	i = 0
	val.append([m[0][0]])
	for r in range(1,n):
		temp = []
		for c in range(len(m[r])):
			if c == 0 :
				temp.append(val[r-1][c] + m[r][c])
			elif c == len(m[r])-1:
				temp.append(val[r-1][c-1] + m[r][c])
			else: 
				temp.append(max(val[r-1][c] + m[r][c], val[r-1][c-1] + m[r][c]))
		val.append(temp)
	# print(m, val)
	return max(val.pop())

input = sys.stdin.readline
t = int(input())
m = []
for i in range(t):
	arr = input()
	m.append([int(a) for a in arr.split()])
print(solution(t, m))