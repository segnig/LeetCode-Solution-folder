class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = Node()
        
    def get(self, index: int) -> int:
        current_node = self.head.next

        while current_node and index:
            current_node = current_node.next
            index -= 1
        if current_node:
            return current_node.val
        return -1

        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

        

    def addAtTail(self, val: int) -> None:
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next  = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        current_node = self.head
        while current_node and index:
            current_node = current_node.next
            index -= 1
        if index or not current_node:
            return 
        new_node.next = current_node.next
        current_node.next = new_node
        
        

    def deleteAtIndex(self, index: int) -> None:
        
        current_node = self.head
        while current_node and index:
            current_node = current_node.next
            index -= 1
        if not current_node or not current_node.next:
            return
        current_node.next = current_node.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)