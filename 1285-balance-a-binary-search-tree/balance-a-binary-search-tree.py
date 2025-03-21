# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sorted_nums = []
        self.dfs(root)
        root = self.create_balanced_tree(self.sorted_nums)

        return root


    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        self.sorted_nums.append(node.val)
        self.dfs(node.right)

    def create_balanced_tree(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.create_balanced_tree(nums[:mid])
        root.right = self.create_balanced_tree(nums[mid + 1:])

        return root