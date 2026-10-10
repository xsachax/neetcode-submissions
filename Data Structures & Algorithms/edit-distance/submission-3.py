class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i, j):
            if j == len(word2):
                return len(word1)-i # count extra letters in word1 as deletions

            if i >= len(word1):
                return len(word2)-j
            
            if (i, j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1, j+1)
                return dp[(i, j)]
            else:
                x1 = 1 + dfs(i, j+1) # insert
                x2 = 1 + dfs(i+1, j) # delete
                x3 = 1 + dfs(i+1, j+1) # replace
            

            dp[(i,j)] = min(x1, x2, x3)
            return dp[(i,j)]

        
        return dfs(0,0)


