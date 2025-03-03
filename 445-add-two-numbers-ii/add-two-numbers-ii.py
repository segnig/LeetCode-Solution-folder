# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.reverser(l1)
        num2 = self.reverser(l2)

        result = None
        carry = 0
        while num1 and num2:
            new_node = ListNode( (num1.val + num2.val + carry) % 10)
            carry = (num1.val + num2.val + carry) // 10
            new_node.next = result
            result = new_node
            num1 = num1.next
            num2 = num2.next

        while num1:
            new_node = ListNode( (num1.val + carry) % 10)
            carry = (num1.val + carry) // 10
            new_node.next = result
            result = new_node
            num1 = num1.next
        
        while num2:
            new_node = ListNode( (num2.val + carry) % 10)
            carry = (num2.val + carry) // 10
            new_node.next = result
            result = new_node
            num2 = num2.next
            
        if carry > 0:
            new_node = ListNode( carry)
            new_node.next = result
            result = new_node

        return result




    def reverser(self, head):
        reversed_num = None
        while head:
            new_node = ListNode(head.val)
            new_node.next = reversed_num
            reversed_num = new_node
            head = head.next
        return reversed_num