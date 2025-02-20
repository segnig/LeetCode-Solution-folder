# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        result = ListNode()
        dummy = result

        seeker = head
        while seeker:
            if seeker.val < x:
                result.next = ListNode(seeker.val)
                result = result.next
            seeker = seeker.next

        seeker = head
        while seeker:
            if seeker.val >= x:
                result.next = ListNode(seeker.val)
                result = result.next
            seeker = seeker.next
        
        return dummy.next   