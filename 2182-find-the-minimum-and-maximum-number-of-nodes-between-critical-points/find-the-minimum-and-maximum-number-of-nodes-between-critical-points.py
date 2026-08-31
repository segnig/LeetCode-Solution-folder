# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        canditate_critical_points = []

        prev, current, nxt = head, head.next, head.next.next 
        index = 1

        while nxt:
            if (nxt.val > current.val and prev.val > current.val) or (nxt.val < current.val and prev.val < current.val):
                canditate_critical_points.append(index)

            prev, current, nxt = current, nxt, nxt.next
            index += 1
        
        ans = [-1, -1]

        if len(canditate_critical_points) > 1:
            ans[1] = canditate_critical_points[-1] - canditate_critical_points[0]

            small = 1000000

            for i in range(1, len(canditate_critical_points)):
                small = min(small, canditate_critical_points[i] - canditate_critical_points[i-1])


            ans[0] = small

        return ans

            

        