# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(lower,node,upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            
            #call on left and right
            left = dfs(lower,node.left,node.val)
            right = dfs(node.val,node.right,upper)
            

            return left and right


        return dfs(float('-inf'),root,float('inf'))