class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        seen = set()


        def dfs(node, prev):
            if node in seen:
                return False

            seen.add(node)

            for nextNode in adj[node]:
                if nextNode == prev:
                    continue
                if not dfs(nextNode, node):
                    return False
            return True
                





        return False if not dfs(0, -1) or n != len(seen) else True
    

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # adj = {i:[] for i in range(n)}
        # for n1, n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)
        
        # visited = set()

        # def dfs(node, prev):
        #     if node in visited:
        #         return False

        #     visited.add(node)
        #     for nextNode in adj[node]:
        #         if nextNode == prev:
        #             continue
        #         if not dfs(nextNode, node):
        #             return False
        #     return True

        


        # return dfs(0, -1) and n == len(visited)

