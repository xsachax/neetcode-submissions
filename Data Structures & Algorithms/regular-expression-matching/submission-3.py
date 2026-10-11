class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if j == len(p):
                return i == len(s)
           

            match = i < len(s) and (p[j] == "." or s[i] == p[j]) 

            if j+1<len(p) and p[j+1] == "*":
                x1 = dfs(i, j+2) # zero occurences
                x2 = match and dfs(i+1, j) # consume one char
                dp[(i,j)] = x1 or x2
            else:
                dp[(i,j)] = match and dfs(i+1, j+1)
            
            return dp[(i,j)]


        return dfs(0,0)