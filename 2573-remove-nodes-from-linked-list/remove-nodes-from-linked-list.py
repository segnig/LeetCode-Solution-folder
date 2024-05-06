# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        store = []
        while temp:
            store.append(temp.val)
            temp= temp.next
        store = store[::-1]
        result = None
        for num in store:
            if not result or result.val <= num:
                new_node = ListNode(num)
                new_node.next = result
                result = new_node
        return result
    