# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def bfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            bfs(node.left)
            bfs(node.right)

        bfs(root)

        return ",".join(res)



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        i = 0

        def build():
            nonlocal i
            if nodes[i] == "N":
                i+=1
                return
            node = TreeNode(int(nodes[i]))
            i+=1
            node.left = build()
            node.right = build()
            return node



        return build()




        




