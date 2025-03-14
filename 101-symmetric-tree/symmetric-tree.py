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
        from_left = self.dfs(root.left, result = [])
        from_right = self.dfs(root.right, left=False, result=[])
        print(from_left, from_right)

        return from_left == from_right
        

    def dfs(self, node, left=True, result=[]):
        if not node:
            result.append(None)
            return result
        result.append(node.val)
        if left:
            self.dfs(node.left, left, result)
            self.dfs(node.right, left, result)
        else:
            self.dfs(node.right, left, result)
            self.dfs(node.left, left, result)
        return result
        

