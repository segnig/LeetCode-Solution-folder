# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        # dfs node, level
        def dfs(node, level):
            # node is null retrun 
            if not node:
                return

            # if no item of that level store
            if len(result) == level:
                result.append(node.val)
                
            # move to both right and left
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        
        dfs(root, 0)
        return result
            