import heapq


def solution(jobs):

    answer = 0
    now = 0  # 현재
    i = 0
    sp = -1  # start point
    heap = []

    while i < len(jobs):
        for job in jobs:
            if sp < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])

        if heap:
            current = heapq.heappop(heap)
            sp = now
            now += current[0]
            answer += now - current[1]
            i += 1
        else:
            now += 1

    return answer//len(jobs)
