class Solution:
    def climbStairs(self, n: int) -> int:
        x1, x2 = 0, 1
        for i in range(1, n+1):
            curr = x1 + x2
            x1 = x2
            x2 = curr

        return curr