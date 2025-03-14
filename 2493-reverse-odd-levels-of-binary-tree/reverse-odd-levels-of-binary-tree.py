# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        is_odd = False
        
        while queue:
            current_level = [node.val for node in queue if node]
            if is_odd:
                for i in range(len(current_level)):
                    queue[i].val = current_level[len(current_level) - i - 1]
            is_odd = not is_odd

            current_level = queue.copy()
            queue = []

            for node in current_level:
                if node:
                    queue.append(node.left)
                    queue.append(node.right)

        return root