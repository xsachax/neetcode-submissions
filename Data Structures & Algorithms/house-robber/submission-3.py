class Solution:
    def rob(self, nums: List[int]) -> int:
        x1, x2 = 0, 0
        for n in nums:
            curr = max(x1+n, x2)
            x1 = x2
            x2 = curr
        
        return curr