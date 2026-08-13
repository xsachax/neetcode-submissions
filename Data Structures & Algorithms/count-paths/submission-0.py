class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        
        def dfs(r, c):
            nonlocal res
            if r in range(m) and c in range(n):
                if r == m-1 and c == n-1:
                    res+=1
                else:    
                    dfs(r+1, c)
                    dfs(r, c+1)

        dfs(0, 0)
        return res