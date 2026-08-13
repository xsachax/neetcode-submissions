# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def count(node):
            if not node:
                return 0
            
            return 1 + count(node.left) + count(node.right)

        def dfs(node, smallerBank):
            if not node:
                return

            smallerValuesOnLeftChild = count(node.left)

            if smallerBank + smallerValuesOnLeftChild + 1 == k:
                return node.val
            
            if node.right and not node.left:
                return dfs(node.right, smallerBank + smallerValuesOnLeftChild+1)
            elif node.left and not node.right:
                return dfs(node.left, smallerBank)

            if smallerValuesOnLeftChild + 1 < k:
                return dfs(node.right, smallerBank + smallerValuesOnLeftChild+1)
            
            else:
                return dfs(node.left, smallerBank)


        return dfs(root, 0)