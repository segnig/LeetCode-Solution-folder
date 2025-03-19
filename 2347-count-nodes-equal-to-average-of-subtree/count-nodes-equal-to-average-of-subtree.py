# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = self.dfs(root)
        return result[2]


    def dfs(self, node):
        if not node:
            return 0, 0, 0
        
        left_count, left_sum, left_result = self.dfs(node.left)
        right_count, right_sum, right_result = self.dfs(node.right) 

        count = left_count + right_count + 1
        result = left_result + right_result
        total_sum = left_sum + right_sum + node.val
        
        mean = total_sum // count

        if mean == node.val:
            result += 1
        return count, total_sum, result     