# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            node = curr.next
            curr = node
        curr = head
        while curr and stack.pop() == curr.val:
            curr = curr.next
        return not curr