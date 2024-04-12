# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            if left[0] and right[0] and abs(right[1] - left[1]) < 2:
                balanced = [True, 1 + max(right[1], left[1])]
            else:
                balanced = [False, 1 + max(right[1], left[1])]
            return balanced
        return dfs(root)[0]
        