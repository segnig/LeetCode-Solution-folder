# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == target and not node.left and not node.right:
                node = None
            
            elif node.left:
                stack.append(node.left)
            elif node.right:
                stack.append(node.right)
        return root
"""
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        if not root.left and not root.right and root.val == target:
            return None
        
        return root
        