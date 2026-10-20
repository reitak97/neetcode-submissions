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
                return
            if node.val >= parentVal:
                self.res +=1
            
            dfs(node.left,max(node.val,parentVal))
            dfs(node.right,max(node.val,parentVal))



     
        dfs(root,float('-inf'))
        return self.res