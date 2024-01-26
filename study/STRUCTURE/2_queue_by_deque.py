from collections import deque

# deque 선언
q = deque()

# enqueue O(1)
q.append(1) # [1]
q.append(2) # [1, 2]
q.append(3) # [1, 2, 3]
q.appendleft(0) # [0, 1, 2, 3]

# dequeue O(1)
q.popleft() # [1, 2, 3]
q.popleft() # [2, 3]
q.pop() # [3]
