class Node:
    def __init__(self, key, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_nodes = {}
        self.elements = {}

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head



    def get(self, key: int) -> int:
        if key not in self.key_nodes:
            return -1
        
        node = self.key_nodes[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        
        node.next = self.tail
        self.tail.prev = node

        self.key_nodes[key] = node

        return self.key_nodes[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_nodes:
            
            node = self.key_nodes[key]
            node.next.prev = node.prev
            node.prev.next = node.next

            node.val = value

            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node

            node.next = self.tail
            self.tail.prev = node

            self.key_nodes[key] = node
            return 



        if len(self.key_nodes) == self.capacity:
            to_delete = self.head.next

            self.head.next = self.head.next.next
            to_delete.next.prev = self.head

            del self.key_nodes[to_delete.key]

        node = Node(key, value)
        
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node

        self.key_nodes[key] = node
        return 


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)