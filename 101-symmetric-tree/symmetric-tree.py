# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)
        

    def dfs(self, node_left, node_right):
        if not node_left or not node_right:
            return node_left == node_right

        if node_left.val != node_right.val:
            return False
        
        left = self.dfs(node_left.left, node_right.right)
        right = self.dfs(node_left.right, node_right.left)
        return left and right 
        

