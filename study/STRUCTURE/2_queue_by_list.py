# queue 선언
q = []

# enqueue O(1)
q.append(1) # [1]
q.append(2) # [1, 2]
q.append(3) # [1, 2, 3]

# dequeue O(n)
q.pop(0) # [2, 3]
q.pop(0) # [3]
