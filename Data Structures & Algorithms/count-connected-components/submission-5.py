class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = list(range(n)) # all nodes are their own parent to start
        size = [1] * n

        def find(x): # find the parent of x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        

        def union(x, y): # make a union between x's group and y's group
            root_x, root_y = find(x), find(y)
            if root_x == root_y: # same parent
                return 0

            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x
            

            parent[root_y] = root_x # attach smaller tree to bigger tree
            size[root_x]+=root_y # update size of new group

            return 1 # + 1 new union



        new_unions = 0
        for src, dst in edges:
            new_unions+= union(src, dst)

        return n - new_unions
        