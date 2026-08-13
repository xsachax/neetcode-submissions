# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        res.append(root.val)
        q = deque()
        q.append(root)
        cycle = []
        while q:
            cycle=[_ for _ in q]
            q.clear()
            
            for c in cycle:
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            if len(q)>0:
                res.append(q[-1].val)
        return res
            
        