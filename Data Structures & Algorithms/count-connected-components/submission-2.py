class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find
        parent = [i for i in range(n)]
        rank = [1] * n # Optimization 1: always attach the smaller tree to the larger one
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x]) # Optimization 2: Path compression
            return parent[x]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0 # we don't need to union here

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] +=1
            else:
                parent[p1] = p2
                rank[p2] +=1
            return 1

    
        res = n
        for src, dst in edges:
            res -= union(src, dst)
        
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # -- DFS --
        # adj = {i:[] for i in range(n)}
        # for x, y in edges:
        #     adj[x].append(y)
        #     adj[y].append(x)
        # seen = set()
        # componentCount = [0]



        # def dfs(node):
        #     if node in seen:
        #         return
        #     seen.add(node)
        #     for i in adj[node]:
        #         dfs(i)


        
        # for i in adj.keys():
        #     if i not in seen:
        #         componentCount[0]+=1
        #         dfs(i)
        
        # return componentCount[0]