# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:


        def dfs(root):
            left, right = False, False

            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            match root.val:
                case 0:
                    return False
                case 1:
                    return True
                case 2:
                    return left or right
                case _:
                    return left and right
        return dfs(root)

        