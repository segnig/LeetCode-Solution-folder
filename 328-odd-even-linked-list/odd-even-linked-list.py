# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next and head.next.next):
            return head

        odd = head 
        even = head.next
        pointer = head.next

        while odd.next.next and even.next.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        if even.next and even.next.next:
            even.next = even.next.next
        elif odd.next and odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
        even.next = None

        odd.next = pointer

        return head




        

        