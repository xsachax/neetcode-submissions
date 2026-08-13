class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            comp = target - v
            if (comp) in seen:
               return sorted([i, seen[comp]])
            seen[v] = i