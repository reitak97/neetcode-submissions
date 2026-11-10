# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if not p and not q:
                return True
            if p and not q or not p and q:
                return False
            if p.val != q.val:
                return False
            return isSame(p.right,q.right) and isSame(p.left,q.left)


        if not root and not subRoot:
            return True
        return isSame(root.left,subRoot) or isSame(root.right,subRoot)