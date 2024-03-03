import sys

check_map = []

def solution(l, m):
	check_map = [[0 for _ in range(l)] for _ in range(l)]
	check_map[0][0] = 1

	r = 0 
	while True:
		if r >= l : break 
		for c in range(l):
			if check_map[r][c] == 0 :continue  
			d = int(m[r][c])
			if d == 0: continue
			if d + r < l :
				check_map[d+r][c] += check_map[r][c]
			if d + c < l :
				check_map[r][d+c] += check_map[r][c]

		r += 1	
	return check_map[l-1][l-1]

input = sys.stdin.readline
t = int(input())
m = []
for i in range(t):
    arr = input()
    m.append(arr.split())
print(solution(t, m))