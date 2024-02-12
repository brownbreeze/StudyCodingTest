class Solution:
    def dp(cost, i):
        if i == 0 :
            return cost[0]
        if i == 1:
            return cost[1]

        return min(dp(cost, i-1)+cost[i-1], dp(cost, i-2)+cost[i-2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return dp(cost, len(cost)-1)