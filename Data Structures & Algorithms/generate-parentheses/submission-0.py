class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(i, j, curr):
            if i == j == n:
                res.append(curr[::])
                return

            if i < n:
                dfs(i+1, j, curr+"(")
            if j < n and j<i:
                dfs(i, j+1, curr+")")

        
        dfs(0, 0, "")

        return res

