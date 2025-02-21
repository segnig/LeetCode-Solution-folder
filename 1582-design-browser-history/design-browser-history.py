class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = Node(homepage)
        self.curr = self.page

    def visit(self, url: str) -> None:
        node = Node(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.curr.prev:
                break
            self.curr = self.curr.prev
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.curr.next:
                break
            self.curr = self.curr.next
        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)