# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.dfs(root)
        return self.result
        


    def dfs(self, node):
        if not node:
            return 0
        left_max = max(self.dfs(node.left), 0)
        right_max = max(self.dfs(node.right), 0)
        self.result = max(self.result, node.val + left_max + right_max)
        
        return node.val + max(left_max, right_max)