# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node,parentVal):
            if not node:
                return 0
            if node.val >= parentVal:
                res = 1
            else:
                res = 0
            
            res = res +dfs(node.left,max(node.val,parentVal)) +dfs(node.right,max(node.val,parentVal))
            
            return res



     
        return dfs(root,float('-inf'))
        