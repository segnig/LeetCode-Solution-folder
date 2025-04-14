# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.dfs(root, head):
            return True
        left = self.isSubPath(head, root.left)
        right = self.isSubPath(head, root.right)
        return left or right

    def dfs(self, node, head):
        if head is None:
            return True
        if not node:
            return False
        if node.val != head.val:
            return False
        
        left = self.dfs(node.left, head.next) 
        right = self.dfs(node.right, head.next)

        return left or right

