# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0

        def dfs(root):

            if not root:
                return []

            if not root.right and not root.left:
                return [1]

            left_dist = dfs(root.right)
            right_dist = dfs(root.left)

            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        self.pairs += 1

            all_dist = left_dist + right_dist

            return [d + 1 for d in all_dist]
        dfs(root)
        return self.pairs

        