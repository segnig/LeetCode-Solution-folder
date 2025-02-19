# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_node = head
        for _ in range(n):
            fast_node = fast_node.next

        if not fast_node:
            return head.next
            
        slow_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next
    
        
        if slow_node.next:
            slow_node.next = slow_node.next.next
        else:
            slow_node.next = None
        
        return head