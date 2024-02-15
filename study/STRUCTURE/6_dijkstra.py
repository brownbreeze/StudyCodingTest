import heapq
import sys


graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: []
}

def dijkstra(graph, start_v, dest_v):
    inf = sys.maxsize
    distances = [inf] * (len(graph)+1)
    # 시작점 예약하기
    # 시작점: 1번노드 / 시작 비용: 0
    pq = []
    heapq.heappush(pq, (0, start_v))
    distances[start_v] = 0

    while pq:
        cur_d, cur_v = heapq.heappop(pq)
        for next_cost, next_v in graph[cur_v]:
            next_d = cur_d + next_cost
            if next_d < distances[next_v]:
                heapq.heappush(pq,(next_d, next_v))
                distances[next_v] = next_d
    return distances[dest_v]

dijkstra(graph, 1, 8)
