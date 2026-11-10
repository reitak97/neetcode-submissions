# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node,parent):
            if not node:
                return 
            if node.val >= parent:
                self.res +=1
            m = max(node.val,parent)
            dfs(node.right,m)
            dfs(node.left,m) 




        dfs(root,float('-inf'))
        return self.res