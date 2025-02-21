class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 
        self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.elements = {}
        self.nodes = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.elements:
            return -1
        
        node = self.nodes[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        
        
        new_node = Node(node.val)
        self.tail.prev.next = new_node
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        
        self.nodes[key] = new_node
          
        return self.elements[key]

    def put(self, key: int, value: int) -> None:
        if key in self.elements:
            self.elements[key] = value
            node = self.nodes[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.nodes.pop(node.val)
            
        else:
            if self.capacity == len(self.elements):
                to_be_deleted = self.head.next
                to_be_deleted.prev.next = to_be_deleted.next
                to_be_deleted.next.prev = to_be_deleted.prev
                
                self.elements.pop(to_be_deleted.val)
            
            self.elements[key] = value
             
        new_node = Node(key)
        self.tail.prev.next = new_node
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        
        self.nodes[key] = new_node
