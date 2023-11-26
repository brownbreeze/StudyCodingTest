from collections import deque
def solution(cards1, cards2, goal):
    goal = deque(goal)
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    while True:
        if len(goal) == 0 : break 
        g = goal.popleft()
        if len(cards1) != 0 and g == cards1[0]:
            cards1.popleft()
            continue
        if len(cards2) != 0 and g == cards2[0]:
            cards2.popleft()
            continue
        return "No"
        
    return "Yes"
