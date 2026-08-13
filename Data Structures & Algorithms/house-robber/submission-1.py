class Solution:
    def rob(self, nums: List[int]) -> int:
        path1, path2 = 0, 0

        for n in nums:
            t = max(path1 + n, path2)
            path1 = path2
            path2 = t
        return path2
        