class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1, 1
        res = float('-inf')

        for n in nums:
            t1 = currMin*n
            t2 = currMax*n

            currMin = min(t1, t2, n)
            currMax = max(t1, t2, n)
            res = max(res, currMax)
        
        return res