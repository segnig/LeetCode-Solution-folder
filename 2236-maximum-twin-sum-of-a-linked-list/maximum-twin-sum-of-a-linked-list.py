# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        temp = head 
        reversed_nums = None
        while temp:
            new_node = ListNode(temp.val)
            new_node.next = reversed_nums
            reversed_nums = new_node
            temp = temp.next

        max_twin = 0

        while head and reversed_nums:
            max_twin = max(max_twin, head.val + reversed_nums.val)
            head = head.next
            reversed_nums = reversed_nums.next
        
        return max_twin
        