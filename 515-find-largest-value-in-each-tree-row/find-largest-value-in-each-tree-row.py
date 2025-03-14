# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        result = []

        while queue:
            current_level = queue.copy()

            current_vals = []
            for node in current_level:
                if node:
                    current_vals.append(node.val)
            if current_vals:
                result.append(max(current_vals))
            queue = []
            for node in current_level:
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        
        return result