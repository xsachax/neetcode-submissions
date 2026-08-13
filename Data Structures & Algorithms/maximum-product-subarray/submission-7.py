class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax = 1
        res = nums[0]
        for n in nums:
            t = n*currMax
            t2 = n*currMin
            currMax = max(t, t2, n)
            currMin = min(t, t2, n)
            res = max(res, currMax)
        return res

        