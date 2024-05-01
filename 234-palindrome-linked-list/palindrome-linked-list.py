# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        fast = None
        while slow:
            fast = ListNode(slow.val, fast)
            slow = slow.next
        slow = fast
        while slow:
            if head.val != slow.val:
                return False
            head, slow = head.next, slow.next
        return True