# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = deque([root])
        while queue:
            current_queue = []
            level_wise = []
            while queue:
                node = queue.popleft()
                if not node:
                    continue
                level_wise.append(node.val)
                if node.left:
                    current_queue.append(node.left)
                if node.right:
                    current_queue.append(node.right)
            queue = deque(current_queue)
            result.append(level_wise)
        return result