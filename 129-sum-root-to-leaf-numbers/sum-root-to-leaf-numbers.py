# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
    
    def dfs(self, node, path_val=0):
        if not node:
            return 0
        path_val = path_val * 10 + node.val

        if not node.left and not node.right:
            return path_val
        
        return self.dfs(node.left, path_val) + self.dfs(node.right, path_val)

    