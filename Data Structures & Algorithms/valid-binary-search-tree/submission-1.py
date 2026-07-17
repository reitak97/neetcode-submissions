# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def isValid(lower,curr,upper):
            if not curr:
                return True
            
            if not(lower < curr.val < upper):
                return False
            
            return isValid(curr.val,curr.right,upper) and isValid(lower,curr.left,curr.val)



        return isValid(float('-inf'),root,float('inf'))