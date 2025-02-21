# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 

        run_node = head
        length = 0
        while run_node:
            run_node = run_node.next
            length += 1
        
        while length >= k:
            count  = 0
            temp = None
            while count < k:
                new_node = ListNode(head.val)
                new_node.next = temp
                temp = new_node
                head = head.next
                count += 1
                length -= 1
            tail.next = temp
            while tail.next:
                tail = tail.next
        tail.next = head

        return dummy.next