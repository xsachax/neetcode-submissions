class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s1, s2 = 0, cost[0]
        for i in range(1, len(cost)):
            cost[i] = cost[i] + min(s1, s2)
            s1=cost[i-1]
            s2=cost[i]
        return min(cost[-1], cost[-2])