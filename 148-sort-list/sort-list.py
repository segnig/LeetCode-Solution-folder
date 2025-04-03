# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.divide(head)
    

    def divide(self, node):
        if not node or not node.next:
            return node

        slow = node
        fast = node

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        right_head = slow.next
        slow.next = None
        
        left = self.divide(node)
        right = self.divide(right_head)
        
        return self.merge(left, right)

    def display(self, node):
        while node:
            print(node.val, "->", end=" ")
            node = node.next
        print()
        

    def merge(self, left_node, right_node):
        merged_node = ListNode(0)
        current = merged_node

        while left_node and right_node:
            if left_node.val <= right_node.val:
                current.next = left_node
                left_node = left_node.next
            else:
                current.next = right_node
                right_node = right_node.next
            current = current.next
        
        if left_node:
            current.next = left_node
        else:
            current.next = right_node
        return merged_node.next

        