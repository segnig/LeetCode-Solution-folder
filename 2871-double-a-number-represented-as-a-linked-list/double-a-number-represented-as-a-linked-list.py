# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        temp = head
        while temp:
            store.append(temp.val)
            temp = temp.next
        result = None
        store = store[::-1]
        carry = 0
        for num in store:
            new_node = ListNode((num + num + carry) % 10)
            carry = (num + num + carry) // 10
            new_node.next = result
            result = new_node
        if carry != 0:
            new_node = ListNode(carry)
            new_node.next = result
            result = new_node
        return result
