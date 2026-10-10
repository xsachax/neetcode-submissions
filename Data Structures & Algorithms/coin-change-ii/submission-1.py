

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, a):
            ways=0
            if a == amount:
                return 1
            if (i, a) in dp:
                return dp[(i, a)]
    

            for j in range(i, len(coins)):
                if a+coins[j]<=amount:
                    ways += dfs(j, a + coins[j])
            
            dp[(i, a)] = ways
            return ways

        return dfs(0, 0)