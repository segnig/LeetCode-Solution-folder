# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not( head and head.next and head.next.next):
            return False

        slow = head.next
        fast = head.next.next
        while fast and fast.next and slow != fast:
            fast = fast.next.next
            slow = slow.next

        if not (fast and fast.next):
            return False
        return True