# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, level):
            if not node:
                return 
            if len(result) - 1 < level:
                result.append(node.val)
            result[level] = max(node.val, result[level])
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        return result