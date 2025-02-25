# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        temp = head 
        reversed_nums = None
        fast = head
        while fast and fast.next:
            temp = temp.next
            fast = fast.next.next
        
        
        while temp:
            new_node = ListNode(temp.val)
            new_node.next = reversed_nums
            reversed_nums = new_node
            temp = temp.next

        max_twin = 0

        while reversed_nums:
            max_twin = max(max_twin, head.val + reversed_nums.val)
            head = head.next
            reversed_nums = reversed_nums.next
        
        return max_twin
        