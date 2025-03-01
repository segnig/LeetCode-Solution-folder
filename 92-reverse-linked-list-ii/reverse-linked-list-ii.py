class Solution: 
    def reverseBetween(self, head, left, right):
        slow=head
        fast=head
        if right==left:
            return head
        for _ in range(left-2):
            slow=slow.next
            fast=fast.next
        if left!=1:
            fast=fast.next
            slow.next=None
        r_tail=fast
        prev=None
        for _ in range(left-1,right):
            if fast:
                temp=fast.next
                fast.next=prev
                prev=fast
                fast=temp
        if left==1:
            head=prev
        else:  
            slow.next=prev
        r_tail.next=fast
        return head
