class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[-1]*(len(s1)+1) for _ in range((len(s2)+1))]

        if len(s1) + len(s2) != len(s3):
            return False
        
        if (not s1 and s2==s3) or (not s2 and s1==s3):
            return True

        def dfs(i, j, k):
            print(i, j, k)

            if i == len(s1) and j==len(s2):
                return 1

            if dp[i][j] == 0 or dp[i][j] == 1:
                return dp[i][j]
            
            x, y = 0, 0
            if i<len(s1) and s3[k] == s1[i]:
                x = dfs(i+1, j, k+1)

            if j<len(s2) and s3[k] == s2[j]:
                y = dfs(i, j+1, k+1)

            
            dp[i][j] = 1 if x+y>=1 else 0
            
            return dp[i][j]

        return True if dfs(0, 0, 0) == 1 else False