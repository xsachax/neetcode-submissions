class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        currMax = nums[0]

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum+= n
            currMax = max(currMax, currSum)
        return currMax