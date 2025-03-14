# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.find_max(root, root.val, root.val)
        return self.result
    
    def find_max(self, node, max_number, min_number):
        if not node:
            return 
        self.result = max(self.result, max(abs(max_number - node.val), abs(min_number - node.val)))
        min_number = min(min_number, node.val)
        max_number = max(max_number, node.val)
        self.find_max(node.left, max_number, min_number)
        self.find_max(node.right, max_number, min_number)