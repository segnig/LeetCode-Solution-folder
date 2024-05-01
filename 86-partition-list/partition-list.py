# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        result = ListNode()
        res = result
        temp = head
        while temp:
            if temp.val < x:
                res.next = ListNode(temp.val)
                res = res.next
            temp = temp.next
        temp = head
        while temp:
            if temp.val >= x:
                res.next = ListNode(temp.val)
                res = res.next
            temp = temp.next
        return result.next