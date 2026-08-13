class Solution:
    def rob(self, nums: List[int]) -> int:
        path1, path2 = 0, 0

        for amount in nums:
             currentMax = max(path1 + amount, path2)
             path1 = path2
             path2 = currentMax
        return currentMax
        