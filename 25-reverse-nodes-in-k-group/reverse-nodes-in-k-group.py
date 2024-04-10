# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.length(head)
        return self.reverser(head, k, length)
        
        
    def length(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def reverser(self, head, k, n):
        if k > n:
            return head
        curr=head
        prev = None
        temp = None
        cnt=0

        while curr is not None and cnt<k:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            cnt+=1

        if temp is not None:
            head.next=self.reverser(temp, k, n-k)

        return prev
