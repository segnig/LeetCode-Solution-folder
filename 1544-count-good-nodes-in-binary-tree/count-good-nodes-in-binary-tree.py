# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        nm  = root.val if root else 0
        def dfs(root, mx):
            nonlocal count
            if not root:
                return
            if mx <= root.val:
                count += 1
            mx = max(mx,  root.val)
            dfs(root.left, mx)
            dfs(root.right, mx)
        dfs(root, nm)
        return count
                
        