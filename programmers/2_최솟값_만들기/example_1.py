def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))

print(getMinSum([1,2],[3,4]))

