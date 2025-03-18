# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find_lowest(root, q.val, p.val)

    def find_lowest(self, node, q_val, p_val):
        if node.val <= max(q_val, p_val) and node.val >= min(q_val, p_val):
            return node

        if node.val < min(q_val, p_val):
            return self.find_lowest(node.right, q_val, p_val)
        else:
            return self.find_lowest(node.left, q_val, p_val)