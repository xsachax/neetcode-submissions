from functools import cache

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for s, d, p in flights:
            adj[s].append([d, p])

        

        res = float('inf')
        seen = set()
        
        @cache
        def dfs(node, stops, total):
            nonlocal res
            if node == dst:
                res = min(res, total)
                return
            
            if stops >= k or node in seen:
                return
            
            stops+=1
            seen.add(node)
            for n, pr in adj[node]:
                dfs(n, stops, total+pr)
            seen.discard(node)

        
        dfs(src, -1, 0)
        return res if res < float('inf') else -1