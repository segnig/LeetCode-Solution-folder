# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverser(root.left, root.right)
        return root

    def reverser(self, left_node, right_node, is_reversed=True):
        if left_node is None:
            return 
        if is_reversed:
            left_node.val, right_node.val = right_node.val, left_node.val
        self.reverser(left_node.left, right_node.right, is_reversed = not is_reversed)
        self.reverser(left_node.right, right_node.left, is_reversed = not is_reversed)
    