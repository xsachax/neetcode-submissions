class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        seen = set()
        componentCount = [0]



        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for i in adj[node]:
                dfs(i)


        
        for i in adj.keys():
            if i not in seen:
                componentCount[0]+=1
                dfs(i)
        
        return componentCount[0]