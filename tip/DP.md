# DP

## Dijkstra

- 최단 경로 탐색 알고리즘

### 설명
- 참고 링크 : https://blog.naver.com/ndb796/221234424646
- 참고 링크 : https://justkode.kr/algorithm/python-dijkstra/

### 소스 예시
```python
graph = {
	'A' : {'B':8, 'C':1, 'D':2},
	'B' : {},
	'C' : {'B':5, 'D':2},
	'D' : {'E':3, 'F':5},
	'E' : {'F':1},
	'F' : {'A':5}
}
import heapq

def dijkstra(graph, start):
	distances = {node:float('inf') for node in graph}
	print(distances)
	distances[start]=0
	queue = []
	heapq.heappush(queue, [distances[start], start])

	while queue:
		current_distance, current_destination = heapq.heappop(queue)

		if distances[current_destination] < current_distance:
			continue

		for new_destination, new_distance in graph[current_destination].items():
			distance = current_distance + new_distance
			if distance < distances[new_destination]:
				distances[new_destination] = distance
				heapq.heappush(queue, [distance, new_destination])

	return distances 

print(dijkstra(graph, 'A'))

```
