# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        root = root.next

        while head:
            root1 = ListNode(val=head.val)
            root1.next = root
            root = root1
            head = head.next
        return root

        
        