# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev_node = head
        current_node = head.next

        while current_node:
            while current_node and prev_node.val == current_node.val:
                current_node = current_node.next

            prev_node.next = current_node
            prev_node = prev_node.next
            if current_node:
                current_node = current_node.next
            

        return head