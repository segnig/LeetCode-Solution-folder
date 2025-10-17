# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True
                
            if not (min_val < node.val < max_val):
                return False
            
            left = dfs(node.left, min_val, node.val)
            right = dfs(node.right, node.val, max_val)
            return left and right
        
        return dfs(root)
        