# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)

    def dfs(self, node_tree1, node_tree2):
        if (node_tree1 is None) and (node_tree2 is None):
            return True
        if not node_tree1 or not node_tree2:
            return False
        if node_tree1.val != node_tree2.val:
            return False
        left = self.dfs(node_tree1.left, node_tree2.left)
        right = self.dfs(node_tree1.right, node_tree2.right)

        return left and right