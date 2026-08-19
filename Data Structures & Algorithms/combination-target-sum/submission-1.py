class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        s = [[0, 0, []]] # [index, sum, subset]
        res = set()

        while s:
            i, ssum, subset = s.pop()

            if i != len(nums):
                if ssum == target:
                    res.add(tuple(subset))
                elif ssum + nums[i] <= target: # add current
                    s.append([i, ssum+nums[i], subset.copy()+[nums[i]]])
                    s.append([i+1, ssum+nums[i], subset.copy()+[nums[i]]])
                s.append([i+1, ssum, subset.copy()])

        return [list(x) for x in res]