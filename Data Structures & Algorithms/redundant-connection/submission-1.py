class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(1, len(edges)+1)}
        seenNodes = set()

        
        def dfs(node, target, visited):
            if node in visited:
                return False
            if node == target:
                return True
            visited.add(node)
            return any(dfs(nextNode, target, visited) for nextNode in adj[node])

        for x,y in edges:
            if x in seenNodes and y in seenNodes:
                if dfs(x, y, set()):
                    return [x,y]
            adj[x].append(y)
            adj[y].append(x)
            seenNodes.add(x)
            seenNodes.add(y)
