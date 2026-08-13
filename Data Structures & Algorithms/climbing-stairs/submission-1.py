class Solution:
    def climbStairs(self, n: int) -> int:
        s1, s2 = 1, 1
        for i in range(n-1):
            nextStep = s1 + s2
            s1 = s2
            s2 = nextStep
        return s2