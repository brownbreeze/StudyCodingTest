- 완전탐색으로 풀기 
source_20240410.py 에서는 이상하게 횟수가 8초과가 아니라 9 초과에서 걸어줘야 정답이었다.
이상하다.. 이상해죽겠다..

source_20240410_2.py에서는 먼저 일단 number가 나오기만 하면, 무조건 답이라는 전제하에 마지만 if return 문을 위치 옮겼고,
list를 중복제거하는 부분을 줄이고, arr와 temp_arr간의 혼선을 줄이니 문제가 횟수 초과를 8 초과로 돌렸을 때 문제가 풀렸다.

정확한 이유는 모르겠지만, temp_arr를 arr로 이동하는 과정에서 어떤 특정 값들을 놓쳤던 것 같다.
