# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res
            if root == None:
                return 0
            
            if abs(dfs(root.left) - dfs(root.right)) > 1:
                res = False
            return 1 + max(dfs(root.left), dfs(root.right))

        
        dfs(root)
        return res

    