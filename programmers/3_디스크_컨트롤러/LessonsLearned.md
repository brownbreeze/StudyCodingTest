- heapq 사용법 
자유로운 추가, 삭제에서 효율적이다.

- 문제 접근법
    - 링크 : https://velog.io/@younge/Python-프로그래머스-디스크-컨트롤러-힙 
    이분이 설명을 잘 간단하게 해놓았다.
    우선순위를 따지는 방식에 대해서 도움이 됐다. 
    "현재 시점에서 처리할 수 있는 작업들을 힙에 넣고 하나를 뽑아 현재 시점과 총 대기시간을 구해주는 것을 모든 작업을 처리할 때까지 반복한다."
    "현재 시점에서 처리할 수 있는 작업인지를 판별하는 조건은 작업의 요청 시간이 바로 이전에 완료한 작업의 시작 시간 보다 크고, 현재 시점보다 작거나 같아야 한다."
    