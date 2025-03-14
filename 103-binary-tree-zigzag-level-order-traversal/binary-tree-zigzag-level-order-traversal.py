# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        is_odd = False
        result = []
        
        while queue:
            current_level = [node.val for node in queue if node]
            if is_odd and current_level:
                result.append(current_level[::-1])
            elif current_level:

                result.append(current_level)

            is_odd = not is_odd

            current_level = queue.copy()
            queue = []
            for node in current_level:
                if node:
                    queue.append(node.left)
                    queue.append(node.right)

        return result