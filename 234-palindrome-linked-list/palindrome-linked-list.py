# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        current = head
        while current:
            node = ListNode(current.val)
            node.next = reverse
            reverse = node
            current = current.next

        while head:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next

        return True