class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr_subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr_subset.copy())
                return
            
            # include current nums[i] path
            curr_subset.append(nums[i])
            dfs(i+1)

            # do not include nums[i] path
            curr_subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res