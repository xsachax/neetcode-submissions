class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax = 1
        res = nums[0]
        for n in nums:
            t = n*currMax
            currMax = max(t, n*currMin, n)
            currMin = min(t, n*currMin, n)
            res = max(res, currMax)
        return res

        