# Copy
list_A = ["ABC","DEF"]
list_B = list_A
list_A = ["ABC","DEF"]
list_B = list_A
list_B.append("GHI")
print(list_A)
# ["ABC","DEF","GHI"]

# 얕은 복사
list1 = [1, 2, 3, 4]
list2 = list1.copy()

# 깊은 복사
import copy
list_A = ["ABC",["DEF","GHI"]]
list_B = copy.deepcopy(list_A)
list_B[1][0] = ["GHI"]
print(list_A, list_B)
# 결과 ['ABC', ['DEF', 'GHI']] ['ABC', [['GHI'], 'GHI']]
