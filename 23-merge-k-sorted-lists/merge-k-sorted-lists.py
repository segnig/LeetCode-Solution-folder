# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        result = ListNode()
        cur = result

        heap = [(head.val, i) for i, head in enumerate(lists) if head]
        heapify(heap)

        while heap:
            val, index = heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            
            if lists[index].next:
                lists[index] = lists[index].next
                heappush(heap, (lists[index].val, index))

        return result.next