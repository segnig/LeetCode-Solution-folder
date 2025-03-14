# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.dfs(root, key)

    def dfs(self, node, val):
        if not node:
            return node
        
        if node.val > val:
            node.left = self.dfs(node.left, val)
        elif node.val < val:
            node.right = self.dfs(node.right, val)
        else:
            
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.minValNode(node.right)
            node.val = temp.val 
            node.right = self.dfs(node.right, temp.val)

        return node

    def minValNode(self, node):
        while node.left:
            node = node.left
        return node
