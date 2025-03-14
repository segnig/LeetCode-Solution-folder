# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        if not head:
            return head
        prev_node = dummy
        next_node = head.next
        self.deleteNode(prev_node, head, next_node, val)
        return dummy.next
        
        
    def deleteNode(self, prev_node, current_node, next_node, val):
        if current_node.val == val:
            prev_node.next = next_node
            if not next_node:
                return 
        else:
            prev_node = current_node
        current_node = next_node
        if next_node:
            next_node = next_node.next
        else:
            return
        self.deleteNode(prev_node, current_node, next_node, val)