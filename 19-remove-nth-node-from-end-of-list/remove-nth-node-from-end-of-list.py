class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode(0)
        node.next = head
        length = -1

        while node:
            length += 1
            node = node.next

        Node = ListNode(0)
        Node.next = head
        node = Node
        c = 0
        while length - c != n:
            Node = Node.next
            c += 1

        Node.next = Node.next.next

        return node.next