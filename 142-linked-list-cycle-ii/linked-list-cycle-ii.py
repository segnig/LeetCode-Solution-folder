# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not( head and head.next and head.next.next):
            return 

        slow = head.next
        fast = head.next.next
        while fast and fast.next and slow != fast:
            fast = fast.next.next
            slow = slow.next

        if not (fast and fast.next):
            return 
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow