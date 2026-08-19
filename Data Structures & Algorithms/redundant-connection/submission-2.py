class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))


        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)

            if root_x == root_y: #already connected, cycle
                return False

            
            parent[root_x] = root_y

            return True

        
        for s, d in edges:
            if not union(s,d): # hit a cycle
                return [s,d]
        return []

            


