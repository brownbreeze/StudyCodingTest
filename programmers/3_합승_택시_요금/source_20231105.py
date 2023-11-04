import heapq

def go_pos(graph, start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_dist, current_dest = heapq.heappop(queue)
        
        if distances[current_dest] < current_dist:
            continue
        for new_dest, new_dist in graph[current_dest].items():
            distance = current_dist + new_dist
            if distance < distances[new_dest]:
                distances[new_dest] = distance
                heapq.heappush(queue, [distance, new_dest])
    return distances
        
def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = dict()
    for i in range(1,n+1):
        graph[i] = dict()        
    
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
    
    first_result = go_pos(graph,s)
    for key, value in first_result.items():
        # print(key, value)
        answer = min(value+ go_pos(graph, key)[b] + go_pos(graph, key)[a], answer)
        # print(go_pos(graph, key)[b])
        # print(go_pos(graph, key)[a])

    return answer
