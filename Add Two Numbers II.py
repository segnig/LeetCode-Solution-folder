# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = ""
        num2 = ''
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next

        res = ''
        carrier = 0

        l = min(len(num1) , len(num2))

        for i in range(l):
            a = int(num1[i])
            b = int(num2[i])
            res = str((a+b + carrier) % 10) + res
            carrier = (a+b + carrier) // 10
        for k in num1[l:]:
            res = str((int(k) + carrier) % 10) + res
            carrier = (int(k) + carrier) // 10

        for k in num2[l:]:
            res = str((int(k) + carrier) % 10) + res
            carrier = (int(k) + carrier) // 10

        if carrier:
            res = str(carrier) + res

        result = ListNode(0)
        resnode = result

        for node in res:
            a = ListNode(node)
            resnode.next = a
            resnode = a

        return result.next
