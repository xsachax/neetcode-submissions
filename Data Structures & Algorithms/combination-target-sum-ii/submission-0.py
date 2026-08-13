class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, total):

            if total == target and subset not in res:
                res.append(subset.copy())
                return

            if i>=len(candidates) or total > target:
                return

            # add current num path
            subset.append(candidates[i])
            dfs(i+1, subset, total+candidates[i])

            subset.pop()
            dfs(i+1, subset, total)


        dfs(0, [], 0)
        return res