# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = [None] * 100
        
        # dfs node, level
        def dfs(node, level):
            # node is null retrun 
            nonlocal max_level
            if not node:
                return
            
            # if no item of that level store
            if result[level] is None:
                result[level] = node.val
            # move to both right and left
            max_level = max(max_level, level + 1)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        max_level = 0
        dfs(root, max_level)
        return result[:max_level]
            