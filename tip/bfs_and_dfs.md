# DFS, BFS

## BFS

- 너비 우선 탐색(Breadth-First Search)

#### 요약

- 최대한 넓게 이동한 다음, 더 이상 갈 수 없을 때 아래로 이동

#### 개념 

- 루트 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법
- 주로 두 노드 사이의 **최단 경로**를 찾고 싶을 때 해당 방식 사용

#### 소스 예시

- queue를 사용한다. 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보만 큐에 넣어 먼저 큐에 들어있던 노드부터 방문한다.
- list가 아닌 queue를 이용하는 이유는 **선입선출**을 위해서는 `list.append(something)`, `list.pop(0)` 와 같이 구현할 수는 있으나, `list.pop(0)` 은 시간복잡도가 *O(N)*이기 때문에 deque를 주로 사용한다.
- 방문하지 않았던 노드를 큐에 넣을 때는 파이썬 타입 중 set을 사용하면 아주 쉽게 구현 가능하다.

```python
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
```

```python
from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
  
print(BFS_with_adj_list(graph_list, root_node))
```



## DFS

- 깊이 우선 탐색(Depth-First Search)

#### 요약

- 최대한 깊이 내려간 뒤, 더이상 깊이 갈 곳이 없을 경우 옆으로 이동

#### 개념

- 루트 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방식
- **모든 노드를 방문**하고자 하는 경우 선택
- 검색 속도 자체는 BFS에 비해 느림

#### 소스 예시

- 스택을 사용한다. 
- 리스트 `stack.append(n)`, `stack.pop()` 를 이용해서 **후입선출**을 이용한다.

```python
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
```

```python
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, root_node))
```



> 참고 
>
> - https://devuna.tistory.com/32
> - https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html