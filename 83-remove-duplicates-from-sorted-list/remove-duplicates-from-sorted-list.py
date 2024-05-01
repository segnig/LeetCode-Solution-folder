# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        nxt = head.next
        while nxt:
            if current.val == nxt.val:
                current.next = nxt.next
                if current:
                    nxt = current.next
                else:
                    return head
            else:
                current, nxt = nxt, nxt.next
        return head