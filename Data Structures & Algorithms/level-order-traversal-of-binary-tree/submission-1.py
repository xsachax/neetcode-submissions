# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lod = []
        def dfs(node, height):
            if node == None:
                return
            nonlocal lod
            print(lod)
            if height >= len(lod):
                lod.append([])    
            lod[height].append(node.val)
            if node.left:
                dfs(node.left, height+1)
            if node.right:
                dfs(node.right, height+1)

        dfs(root, 0)
        return lod


